<h1 id="5-반복문">5. 반복문</h1>
<h2 id="1for">1.for</h2>
<p>주어진 횟수만큼 반복하여 실행하는 구조!</p>
<pre><code>for (초기치;조건문;증가치){
    반복하여 실행 할 내용;
}</code></pre><h2 id="2while">2.while</h2>
<p>조건문이 만족하는동안 반복하여 실행하는 구조
while과 do-while 구조가 있음.</p>
<pre><code>while(조건문){
반복하여 실행 할 내용;
}

do{
    반복하여 실행 할 내용;
}while(조건문);
</code></pre><pre><code class="language-java">package java_05;

// Java 프로그래밍 - 반복문

public class Main {
    public static void main(String[] args) {

//      1. 반복문 - for
        System.out.println(&quot;== for ==&quot;);
//      1-1. 기본 사용 방법
        for (int i = 0; i&lt;5; i++){
            System.out.println(i);
        }
        for (int i = 0; i&lt;5; i++){
            for (int j = 0; j&lt;i+1; j++){
                System.out.print(&quot;*&quot;);
            }
            System.out.println();
        }

        System.out.println();
        System.out.println();
        for (int i = 0; i&lt;5; i++){
            if (i ==2){
                continue;
                //이 밑 코드는 실행하지 않고 다음으로 넘어간다
            }
            for (int j = 0; j&lt;i+1; j++){
                System.out.print(&quot;*&quot;);
            }
            System.out.println();
        }
        System.out.println();
        System.out.println();
        for (int i = 0; i&lt;5; i++){
            if (i ==2){
                break;
                //반복문 바로 탈주!!
            }
            for (int j = 0; j&lt;i+1; j++){
                System.out.print(&quot;*&quot;);
            }
            System.out.println();
        }

        System.out.println();
//      1-2. for each
        int[] nums = {1,2,3,4,5};
        for (int i = 0; i &lt; nums.length; i++) {
            System.out.println(nums[i]);
        }

        System.out.println();
        System.out.println();

        for (int temp : nums){
            System.out.println(temp);
        }


//      2. 반복문 - while
        System.out.println(&quot;== while ==&quot;);
//      2-1. while
        int i = 0;
        while (i &lt;5){
            System.out.println(i);
            i++;
        }

        i= 0;
        while (i&lt;5){
            if (i==2){
                i++;
                continue;
                //증가만 하고 출력 ㄴㄴ
            }
            System.out.println(i++);
        }

  i= 0;
        while (i&lt;5){
            if (i==2){
                i++;
                break;
                //탈주
            }
            System.out.println(i++);
        }



//      2-2. do-while
        boolean flag = false;
        do {
            System.out.println(&quot;knock&quot;);
        }while (flag);


//      Q1. 아래와 같은 출력 결과를 반복문과 조건문을 이용하여 출력해보세요.
//      *
//      ***
//      *****
//      *******

        for (int j = 0 ; j&lt;8; j++){
            if (j%2==0){
                continue;
            }
            for (int k = 0; k &lt; j; k++) {

                System.out.print(&quot;*&quot;);
            }
            System.out.println();
        }




//      Q2. 반복문을 실행할 때마다 물 온도를 1도씩 올리고 100도가 되면 종료한다.
//          추가로, 10도, 20도, ... 10도 간격으로 물 온도를 출력하시오.
        int waterTemperature = 0;


        while (waterTemperature&lt;100){
            waterTemperature++;
            if (waterTemperature%10==0){
                System.out.println(waterTemperature);
            }
        }

    }
}
</code></pre>