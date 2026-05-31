<script setup>

import UserInfoField from "@/views/user/space/components/UserInfoField.vue";
import {nextTick, onBeforeUnmount, onMounted, ref, useTemplateRef} from "vue";
import api from "@/js/http/api.js";
import {useRoute} from "vue-router";
import Character from "@/components/character/Character.vue";


const userProfile = ref(null)
const characters = ref([])
const isLoading = ref(false)
const hasCharacters = ref(true)
const sentinelRef = useTemplateRef('sentinel-ref')
const route = useRoute()


function checkSentinelVisible() {  // 判断哨兵是否能被看到
  if (!sentinelRef.value) return false

  const rect = sentinelRef.value.getBoundingClientRect()
  return rect.top < window.innerHeight && rect.bottom > 0
}

async function loadMore(){
  if (isLoading.value || !hasCharacters.value) return
  isLoading.value = true

  let newCharacters = []
  try {
    const res = await api.get('/api/create/character/get_list/',{
      params: {     // get的参数一定要 放在 params 里面
        items_count: characters.value.length,
        user_id: route.params.user_id,
      }
    })
    const data = res.data
    //console.log(data)
    if (data.result === 'success') {
      userProfile.value = data.user_profile
      newCharacters = data.characters
    }
  } catch(err) {
    console.log(err)
  } finally {
    isLoading.value = false
    if (newCharacters.length === 0) {
      hasCharacters.value = false
    }
    else {
      characters.value.push(...newCharacters)  // ...是为了把列表展开
      await nextTick()

      if (checkSentinelVisible()) {
        await loadMore()
      }
    }
  }
}

// 监听器，监听哨兵和视窗有没有交叉
let observer = null
onMounted(async () =>{
  await loadMore()

  observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          loadMore()
        }
      })
    },
    {root: null, rootMargin: '2px', threshold: 0}
  )
  observer.observe(sentinelRef.value)
})

// 在列表里删除
function removeCharacter(characterId) {
  characters.value = characters.value.filter(c => c.id !== characterId)  // 把所有不等于characterId取出来，其他删掉
}

onBeforeUnmount(() => {
  observer?.disconnect()
})


</script>

<template>
  <div class="flex flex-col items-center mb-12 ">
    <UserInfoField :userProfile="userProfile" />
    <div class="grid grid-cols-[repeat(auto-fill,minmax(240px,1fr))] gap-9 mt-12 justify-items-center w-full px-9">
      <Character
        v-for="character in characters"
        :key="character.id"
        :character="character"
        :canEdit="true"
        @remove="removeCharacter"
      />
    </div>

      <!--    // 下面是流式加载-->
      <!--    // 定义哨兵-->
    <div ref="sentinel-ref" class="h-2 mt-8"></div>
    <div v-if="isLoading" class="text-gray-500 mt-4">加载中...</div>
    <div v-else-if="!hasCharacters" class="text-gray-500 mt-4">没有更多角色了</div>
  </div>
</template>

<style scoped>

</style>