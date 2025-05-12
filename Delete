![baner](https://github.com/Ghosts6/Local-website/blob/main/img/Baner.png)

#  💫Description:
some useful script with c c++ python to restart or shutdown system in different os
# 📴shutdown_script:
#python :

```python
import os

def main():
    choice = input("select operation type?(shutdown/restart)")
    if choice == "shutdown" or choice == "shutdown":
        shutdown()
    elif choice == "restart" or choice == "Restart":
        restart()
    else:
        print("wrong choice please try again .")
        main()

def shutdown():
    shutdown = input("do you want to shutdown system(yes/no)?")
    if shutdown == "yes" or shutdown == "Yes" :
        os.system("shutdown /s /t 1") 
        os.system("sudo poweroff")
        os.system("shutdown now -h")
    elif shutdown == "no":
        exit()


def restart():
    restart = input("do you want restart system(yes/no)")
    if restart == "yes"  or restart == "Yes" :
        os.system("sudo reboot")
        os.system("shutdown /r")
        os.system("shutdown -r -t 0")
    elif restart == "no" :
        exit()

main()
```
#c++:

```cpp
#include <iostream>
#include <string>
using namespace std;
int main(){
    char choice;
    string choice_2;
    cout<<"do you want restart or shutdown for restart type r for shutdown type s"<<endl;
    cin>>choice;
    jump:
if(choice == 'r' || choice == 'R'){
    system("shutdown -r -t 0");
    system("sudo reboot");
    system("c:\windows\system32\shutdown /r ");
}
if(choice == 's' || choice == 'S'){
    system("sudo poweroff");
    system("shutdown -P now");
    system("c:\windows\system32\shutdown /i ");
}
else{
    cout<<"wrong input"<<'\n'<<"do you want to try again?(yes/no)"<<endl;
    cin>>choice_2;
}
if(choice_2 == "yes" || choice_2 == "Yes"){
    goto jump;
}
else{
    cout<<"end of program"<<endl;
}
    return 0;
}
```
#c:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void shutdown();
void restart();

int main() {
    char choice[20]; 
    label:
    printf("Select operation type (restart/shutdown) \n"); 
    scanf("%s", choice); 
    if (strcmp(choice, "restart") == 0 || strcmp(choice, "Restart") == 0) {
        restart();
    }
    else if (strcmp(choice, "shutdown") == 0 || strcmp(choice, "Shutdown") == 0) { 
        shutdown();
    }
    else {
        printf("wrong choice please try again \n");
        goto label;
    }
    printf("End of program\n");
    return 0;
}

void shutdown(){
    #ifdef _WIN32
        system("shutdown /s");
    #elif __unix__
        system("sudo poweroff");
    #elif __linux__
        system("sudo poweroff");
    #endif
}

void restart(){
    #ifdef _WIN32
        system("shutdown /r");
    #elif __unix__
        system("sudo reboot");
    #elif __linux__
        system("sudo reboot");
    #endif
}
```

