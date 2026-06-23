from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character
from web.models.friend import Friend, Message, SystemPrompt


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)       # 逗号不要删！！！



@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    rea_id_fields = ('me', 'character',)       # 把外键加到这里


@admin.register(Message)
class MessagesAdmin(admin.ModelAdmin):
    rea_id_fields = ('friend',)

admin.site.register(SystemPrompt)
# 不包含外键，直接注册就行了