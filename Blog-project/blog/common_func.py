from blog.models import UserPermission


def checkUserPermission(request,access_type,menu_url, obj_owner=None):
    if not request.user.is_authenticated:
        return False
    
     # 1️⃣ Superuser → full access
    if request.user.is_superuser:
        return True

    # 2️⃣ Owner of object → full access
    if obj_owner and obj_owner == request.user:
        return True
    try:
        
        user_permission = {
            "can_view":"can_view",
            "can_add":"can_add", 
            "can_edit":"can_edit",
            "can_delete":"can_delete"
        }
        
         # Invalid access type
        if access_type not in user_permission:
            return False
    
        check_user_permission = UserPermission.objects.filter(
            user_id =request.user.id,
            is_active=True,
            menu__menu_url=menu_url,
            **{user_permission[access_type]:True}, 
        )
        
        print(check_user_permission)
        if check_user_permission.exists():
            return True
        else:
            return False
        
    except Exception as e:
        print("Permission error:", e)
        return False    