# Star
```def star(d)``` โดยที่ d คือเส้นผ่านศูนย์กลางของดาว ต้องเป็น int มีค่าเป็นบวก และเป็นเลขคี่ ให้คืนค่าเป็น String ถ้าไม่ตรงเงื่อนไขให้คืนค่า ```Error``` 

#### Hint
1. x^2 + y^2 = r^2
2. ไม่มี ```'\n'``` ตอนท้ายสุด
3. มี ```' '``` แค่ในรูปดาว

#### Example

star(5) >>
```
#######
### ###
### ###
#     #
### ###
### ###
#######
```

star(27) >>
```
#############################
############## ##############
############## ##############
############## ##############
############## ##############
############## ##############
#############   #############
#############   #############
############     ############
###########       ###########
##########         ##########
#########           #########
########             ########
######                 ######
#                           #
######                 ######
########             ########
#########           #########
##########         ##########
###########       ###########
############     ############
#############   #############
#############   #############
############## ##############
############## ##############
############## ##############
############## ##############
############## ##############
#############################
```

star(31) >>
```
#################################
################ ################
################ ################
################ ################
################ ################
################ ################
###############   ###############
###############   ###############
##############     ##############
##############     ##############
#############       #############
############         ############
###########           ###########
##########             ##########
########                 ########
######                     ######
#                               #
######                     ######
########                 ########
##########             ##########
###########           ###########
############         ############
#############       #############
##############     ##############
##############     ##############
###############   ###############
###############   ###############
################ ################
################ ################
################ ################
################ ################
################ ################
#################################
```
