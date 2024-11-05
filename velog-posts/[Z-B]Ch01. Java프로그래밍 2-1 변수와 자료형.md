<h1 id="2-1변수와-자료형">2-1.변수와 자료형</h1>
<h2 id="1변수-개념">1.변수 개념</h2>
<p>변수(Variable)?
데이터를 저장하는 메모리 공간에 붙여준 이름.</p>
<pre><code class="language-java">int age = 20;
String country = &quot;Korea&quot;;</code></pre>
<h2 id="2변수-이름-규칙">2.변수 이름 규칙</h2>
<p><img alt="" src="https://velog.velcdn.com/images/noop/post/4f6c896b-cc84-467f-aae3-f87d56532caf/image.png" /></p>
<h2 id="3표기법">3.표기법</h2>
<ol>
<li>카멜 표기법(camelCase)</li>
</ol>
<ul>
<li>가장 앞의 문자는 소문자로, 나머지 단어의 첫 문자는 대문자로 표기.
ex)myName, zeroBase , iPhone...</li>
</ul>
<ol start="2">
<li>파스칼 표기법(PascalCase)</li>
</ol>
<ul>
<li>각 문자의 첫 문자를 대문자로 표기
ex) MyName,ZeroBase...</li>
</ul>
<pre><code class="language-java">package java_02_1;
// Java 프로그래밍 - 변수와 자료형_1

public class Main {
    public static void main(String[] args) {

//      1. 변수 사용하기
        System.out.println(&quot;== 변수 사용하기 ==&quot;);
        int age =10;
        System.out.println(&quot;age = &quot; + age);
        String country =&quot;Korea&quot;;
        System.out.println(&quot;country = &quot; + country);

//      2. 변수 이름 규칙
        System.out.println(&quot;== 변수 이름 규칙 ==&quot;);
//      2-1. 문자, 숫자, _(underscore), $ 사용 가능
        int apple = 2000;
        int apple3 = 2000;
        int _apple = 2000;
        int $apple = 2000;

        System.out.println($apple);
        System.out.println(&quot;$apple = &quot; + $apple);

//      2-2. 숫자로 시작 X

        //int 3apple = 2000;



//      2-3. 대소문자 구분
        int apple5 = 1000;
        int Apple5 = 2000;
//      2-4. 공백 사용 X

        int one_apple = 0;
        int oneApple = 1000;

//      2-5. 예약어 사용 X
//      예약어 예시: true, false, if, switch, for, continue, break, ...
        //int true = 1;
//      참고) 한글 사용 가능
        int 사과 = 1000;
        System.out.println(&quot;사과 = &quot; + 사과);

//      3. 표기법
//      3-1. 카멜 표기법 (camelCase)
//      변수, 함수

        int myAge = 10;
        int oneApplePrice = 1000;

//      3-2. 파스칼 표기법 (PascalCase)
//      클래스
        int MyAge = 10;

//      참고) 스네이크 표기법 (snake_case)
//      사용 X

        int my_age = 10;

    }
}

</code></pre>