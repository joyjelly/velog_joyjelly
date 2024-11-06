<h1 id="4-조건문">4. 조건문</h1>
<h2 id="1if">1.if</h2>
<h3 id="조건에-따라-무엇을-실행할지-판단하는-분기구조">조건에 따라 무엇을 실행할지 판단하는 분기구조</h3>
<h2 id="2switch">2.switch</h2>
<h3 id="입력-값에-따라-어떤-case를-실행-할지-판단하는-분기구조">입력 값에 따라 어떤 case를 실행 할지 판단하는 분기구조</h3>
<pre><code class="language-java">switch(입력값){
    case 입력값 1:
    실행 할 내용;
    break;

    case 입력값 2:
    실행 할 내용;
    break;
    .
    .
    .
    default:
    실행 할 내용;
    break;
}</code></pre>
<pre><code class="language-java">package java_04;
// Java 프로그래밍 - 조건문

public class Main {
    public static void main(String[] args) {

//      1. 조건문 - if
        System.out.println(&quot;== if ==&quot;);

        int waterTemperature = 99;

        if(waterTemperature &gt;=100){
            System.out.println(&quot;물이 끓습니다&quot;);
        }else {
            System.out.println(&quot;물을 끓이는 중입니다&quot;);

        }

        int score = 60;
        char grade = 0;

        if (score &gt;=90){
            grade = 'A';
        } else if (score &gt;= 80) {
            grade = 'B';

        } else if (score &gt;= 70) {
            grade = 'C';

        }else {
            grade = 'F';
        }
        System.out.println(&quot;grade = &quot; + grade);

//      2. 조건문 - switch
        System.out.println(&quot;== switch ==&quot;);

        String fruit = &quot;apple2&quot;;

        switch (fruit){
            case &quot;apple&quot; :
                System.out.println( fruit+&quot; 은 5000원 입니다&quot;);
                break;

            case &quot;blueberry&quot;:
                System.out.println( fruit+&quot; 은 10000원 입니다&quot;);
                break;

            default:
                System.out.println(&quot;해당 과일이 없습니다&quot;);
                break;
        }


//      Q1. number의 값이 홀수인지 짝수인지 판단하는 코드를 작성하세요.
        int number = 5;

        if (number %2 ==0){
            System.out.println(&quot;짝수입니다&quot;);
        }else {
            System.out.println(&quot;홀수입니다&quot;);

        }


//      Q2. 아래 주석은 위의 실습에서 진행한 score에 따라 grade를 출력하는 코드이다.
//        이를 switch 조건문 기반으로 바꿔보세요.
          score = 90;
             grade = 0;
//        if (score &gt;= 90) {
//            grade = 'A';
//        } else if (score &gt;= 80) {
//            grade = 'B';
//        } else if (score &gt;= 70) {
//            grade = 'C';
//        } else {
//            grade = 'F';
//        }
//        System.out.println(&quot;grade = &quot; + grade);

        switch (score/10){
            case 9 :
                grade ='A';
                break;
             case 8 :
                grade ='B';
                break;
             case 7 :
                grade ='C';
                break;
            default:
                grade = 'F';
                break;
        }
        System.out.println(&quot;grade = &quot; + grade);
    }

}
</code></pre>