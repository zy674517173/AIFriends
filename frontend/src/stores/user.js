import {defineStore} from "pinia";
import {computed, ref} from "vue";

export const userUserStore = defineStore('user', () => {
    const id = ref(0)
    const username = ref('')
    const photo = ref('')
    const profile = ref('')
    const accessToken = ref('')

    // 判断是不是登录了
    function isLogin(){
        return !!accessToken.value    // 必须带 value!!!!!!!!!!!
        // ！一次把空列表、0、空字符串变成false
    }

    // 用于设置accessToken
    function setAccessToken(token){
        accessToken.value = token
    }

    function setUserInfo(data){
        id.value = data.user_id
        username.value = data.username
        photo.value = data.photo
        profile.value = data.profile
    }

    function logout(){
        id.value = 0
        username.value = ''
        photo.value = ''
        profile.value = ''
    }

    return {
        id,
        username,
        photo,
        profile,
        accessToken,            // 千万不要忘记!!!  否则
        isLogin,
        setAccessToken,
        setUserInfo,
        logout
    }
})
