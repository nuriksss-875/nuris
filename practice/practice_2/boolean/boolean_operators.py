
has_id = input("Do you have an ID? (yes/no): ") == "yes"
has_invitation = input("Do you have an invitation? (yes/no): ") == "yes"
is_vip = input("Are you a VIP guest? (yes/no): ") == "yes"
is_banned = input("Are you banned? (yes/no): ") == "yes"

# Entry logic
can_enter = (has_id and has_invitation) or (is_vip and not is_banned)

print("Has ID:", has_id)
print("Has invitation:", has_invitation)
print("VIP:", is_vip)
print("Banned:", is_banned)
print("Can enter:", can_enter)