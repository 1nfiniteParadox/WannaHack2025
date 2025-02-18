#include <stdio.h>
#include <stdlib.h>

int main(){
    puts(" ██████╗██╗  ██╗███████╗ █████╗ ██████╗      █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗"); 
    puts("██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║"); 
    puts("██║     ███████║█████╗  ███████║██████╔╝    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║");  
    puts("██║     ██╔══██║██╔══╝  ██╔══██║██╔═══╝     ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║");
    puts("╚██████╗██║  ██║███████╗██║  ██║██║         ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║");
    puts(" ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝         ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝");
    setbuf(stdout, NULL);
    int balance = 1000;
    int money = 0;
    printf("Welcome! Buy whatever you want, but remember to check your balance.\n");
    while(1){
        printf("\n");
        printf("Money in pocket: %d\n", money);
        printf("Current Amazon Balance: %d\n", balance);
        printf("1. Withdraw\n");
        printf("2. Deposit\n");
        printf("3. Buy flag (PRICE: 1000000)\n");
        printf("4. Exit\n");
        int input;
        int option;
        printf("Option: ");
        scanf("%d", &option);
        if(option == 1){
            printf("Enter amount of money to withdraw: ");
            scanf("%d", &input);
            if(input <= balance) {
                balance -= input;
                money += input;
            }
            else {
                printf("Not enough balance!\n");
                continue;
            }
        }
        else if(option == 2){
            printf("Enter amount of money to deposit: ");
            scanf("%d", &input);
            if(input <= money) {
                balance += input;
                money -= input;
            }
            else {
                printf("Not enough money!\n");
                continue;
            }
        }
        else if(option == 3){
            if(money < 1000000) printf("Not enough money!\n");
            else {
		system("cat /flag.txt");
                return 0;
            }
        }
        else if(option == 4){
            return 0;
        }
        else{
            printf("Not a valid option!");
        }
    }
    return 0;
}
