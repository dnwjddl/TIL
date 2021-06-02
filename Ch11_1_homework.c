//2번
#include <stdio.h>

void get_sum_diff(int x, int y, int *sum_2, int *diff_2){ //합과 차를 구하는 함수
    *sum_2 = x+y; //integer x와 y의 합
    *diff_2 = x-y; //integer x와 y의 차
    return; //반환해주지 않아도 포인터를 통해서 반환 가능
}

int main(){
    int a, b; //두 수 초기화
    int sum, diff; //합과 차 초기화

    scanf("%d %d", &a, &b); //두 수 입력
    get_sum_diff(a,b, &sum, &diff);  //get_sum_diff의 함수를 사용해서 sum와 diff를 주소의 값으로 불러옴
    printf("원소들의 합=%d\n", sum); //두 수의 합
    printf("원소들의 차=%d\n", diff); // 두 수의 차

    return 0;
}

//4번

#include <stdio.h>
#define SIZE 5 //정수 배열의 크기 상수 

void print_array(int *A, int size){ // 정수 배열 초기화
    printf("A[]={ "); 
    for(int i = 0; i< size; i++) //포인터를 사용해서 배열 하나씩 printf
        printf("%d ", A[i]); //배열의 원소 하나씩 출력
    printf("}");
    return; //포인터를 사용해서 값을 반환할 필요없음
}

int main(){
    int array[SIZE] = {1,2,3,4,0};  //배열 초기화
    print_array(array, SIZE); //배열 출력

    return 0;
}

//6번
#include <stdio.h>
#define SIZE 5 //SIZE 상수값 10으로 초기화

void array_copy(int *A, int *B, int size) { //배열의 값을 copy
    for(int i = 0; i<size; i++)
        B[i] = A[i]; //원소 하나씩 B의 배열로 copy함
}

void print_array(int *A, int size){ //4번의 print_array 함수와 동일
    printf("A[]= ");
    for(int i = 0; i< size; i++)
        printf("%d ", A[i]);
    printf("\n");
    return;
}


int main(){
    int a[SIZE] = {1,2,3,4,5};
    int b[SIZE] = {5,4,3,2,1};
    print_array(a, SIZE); //a의 배열 초기화
    array_copy(a,b,SIZE); //배열 Copy해서 b로 가지고옴(포인터 사용)
    print_array(b, SIZE); //포인터를 사용했기 때문에 b를 바로 불러올 수 있음

    return 0;
}
