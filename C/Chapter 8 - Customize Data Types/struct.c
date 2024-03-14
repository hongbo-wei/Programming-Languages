#include <stdio.h>

int main()
{
    struct Student
    {
        long int num;
        char name[20];
        char sex;
        char addr[20];
    } student1 = {594007, "Hongbo Wei", 'M', "Guizhou"};

    printf("No. %ld\nName: %s\nSex: %c\nAddress: %s\n",
           student1.num, student1.name, student1.sex, student1.addr);
}