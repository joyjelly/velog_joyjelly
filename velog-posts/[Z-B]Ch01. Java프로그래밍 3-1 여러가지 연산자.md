<h1 id="3-1-여러가지-연산자">3-1. 여러가지 연산자</h1>
<h2 id="1-항과-연산자">1. 항과 연산자</h2>
<h3 id="단항-연산자--항이-한개">단항 연산자 : 항이 한개</h3>
<p>ex) num++</p>
<h3 id="2-이항-연산자--항이-두개">2. 이항 연산자 : 항이 두개</h3>
<p>ex) 1+1</p>
<h3 id="3-삼항-연산자--항이-세개">3. 삼항 연산자 : 항이 세개</h3>
<p>ex) (3&gt;1) ? 1:0</p>
<h2 id="2-대입-연산자-부호-연산자">2. 대입 연산자, 부호 연산자</h2>
<h3 id="대입-연산자">대입 연산자</h3>
<p>우측의 데이터를 좌측의 변수에 대입
ex) int num = 100;</p>
<h3 id="부호연산자">부호연산자</h3>
<p>부호를 나타내는 연산자
ex) +10, -10</p>
<h2 id="3-산술-연산자증가감소-연산자">3. 산술 연산자,증가/감소 연산자</h2>
<h3 id="산술연산자">산술연산자</h3>
<p>덧셈 뺄셈 곱셈 나눗셈 나머지</p>
<h3 id="증감연산자">증감연산자</h3>
<p>값을 1만큼 늘리거나 1만큼 줄임
ex) num++; ++num;</p>
<h2 id="4-관계-연산자">4. 관계 연산자</h2>
<ol>
<li><p>두 항의 값 크기 비교</p>
</li>
<li><p>결과 값은 비교 결괴에 따라 true 또는 false
ex)
10 &gt; 9
5 !=3</p>
</li>
</ol>
<h2 id="5-논리-연산자----">5. 논리 연산자 (&amp;&amp;, || , !)</h2>
<ol>
<li>논리식에 대해 참 거짓 판단</li>
<li>결과 값은 판단 결과에 따라 true 또는 false
ex) (10&gt;9) &amp;&amp; (1 == 0)</li>
</ol>
<p>ex) (10&gt;9) || (1 == 0)</p>
<h2 id="6-복합-대입-연산자">6. 복합 대입 연산자</h2>
<ol>
<li><p>대입 연산자와 다른 연산자를 조합한 연산</p>
</li>
<li><p>코드를 간결하게 작성 할 때 사용
ex) num1 += num2;
ex) num1 %= num2;</p>
</li>
</ol>
<pre><code class="language-java">package java_03_01;
// Java 프로그래밍 - 여러가지 연산자_1

public class Main {
    public static void main(String[] args) {

//      1. 대입 연산, 부호 연산자
        int num = 100;
        num = +10;
        num =10;
        num = -10;

//      2. 산술 연산자, 증가/감소 연산자
        System.out.println(&quot;== 산술 연산자, 증가/감소 연산자 ==&quot;);

        int numX = 10;
        int numY = 3;
        int result = 0;
        result = numX+numY;
        result = numX-numY;
        result = numX*numY;
        result = numX/numY;
        result = numX%numY;
        System.out.println(&quot;result = &quot; + result);

        int numz =1;
        //원래 값을 출력 한 후에 값에 1을 더한다
        System.out.println(numz++);

        System.out.println(numz);


        numz =1;
        System.out.println(++numz);
        System.out.println(numz);

        numz =1;
        System.out.println(numz--);
        System.out.println(numz);

        numz =1;
        System.out.println(--numz);
        System.out.println(numz);


//      3. 관계 연산자
        System.out.println(&quot;== 관계 연산자 ==&quot;);

        int numA = 10;
        int numB = 9;

        System.out.println(numA &gt; numB);
        System.out.println(numA &lt; numB);
        System.out.println(numA == numB);
        System.out.println(numA != numB);


//      4. 논리 연산자
        System.out.println(&quot;== 논리 연산자 ==&quot;);

        //둘다 맞아야
        System.out.println((10&gt;9) &amp;&amp;(1 ==0));
        System.out.println((10&gt;9) ||(1 ==0));

//      5. 복합 대입 연산자
        System.out.println(&quot;== 복합 대입 연산자 ==&quot;);

        int num1 = 10;
        int num2 = 5;
        //num1 = num1+num2
        num += num2;
        System.out.println(&quot;num1 = &quot; + num1);



//      6. 삼항 연산자
        System.out.println(&quot;== 삼항 연산자 ==&quot;);



        int a =100;
        String aResult  = (a==100)? &quot;yes&quot; : &quot;no&quot;;
        System.out.println(&quot;aResult = &quot; + aResult);
    }

}
</code></pre>