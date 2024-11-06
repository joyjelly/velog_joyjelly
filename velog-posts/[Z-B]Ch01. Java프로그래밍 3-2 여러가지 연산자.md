<h1 id="3-2-여러가지-연산자">3-2. 여러가지 연산자</h1>
<h2 id="1-이진법">1. 이진법</h2>
<h3 id="이진법">이진법</h3>
<p>컴퓨터에서 데이터 표현에 사용
2를 기반으로 하는 숫자 체계</p>
<h3 id="2의-보수">2의 보수</h3>
<p>2의 제곱수에서 빼서 얻은 이진수
ex) 
10진수에서는 3의 보수는 7이다 -&gt; 자릿수가 바뀜 
2진수에서 3의 2 보수 -&gt; 01</p>
<h2 id="2-비트-연산자">2. 비트 연산자</h2>
<h3 id="비트단위로-연산">비트단위로 연산</h3>
<h3 id="기본-연산자와-비트-연산자-비교">기본 연산자와 비트 연산자 비교</h3>
<h2 id="3-비트-논리-연산자">3. 비트 논리 연산자</h2>
<h3 id="and-연산자-">AND 연산자 (&amp;)</h3>
<ul>
<li>두개의 비트 값이 모두 1인 경우에만 결과 1
ex)
0011
0101</li>
<li><blockquote>
</blockquote>
0001</li>
</ul>
<h3 id="or-연산자-">OR 연산자 (|)</h3>
<p>두개의 비트 값 중 하나라도 1이면 결과 1
ex)
0011
0101
-&gt;
0111</p>
<h3 id="xor-연산자-">XOR 연산자 (^)</h3>
<p>두 개의 비트 값이 같으면 0, 다르면 1</p>
<p>ex)
0011
0101
-&gt;
0110</p>
<h3 id="반전연산자-">반전연산자 (~)</h3>
<p>비트값이 0이면 1로, 1이면 0으로 반전</p>
<h2 id="4-비트-이동-연산자">4. 비트 이동 연산자</h2>
<h3 id="연산자">&lt;&lt;연산자</h3>
<p>비트를 왼쪽으로 이동
ex) 3&lt;&lt;1
0011
0110</p>
<h3 id="연산자-1">&gt;&gt;연산자</h3>
<p>비트를 오른쪽으로 이동
ex) 3&gt;&gt;1
0011
0001</p>
<h3 id="연산자-2">&gt;&gt;&gt;연산자</h3>
<p>비트를 오른쪽으로 이동</p>
<pre><code class="language-java">package java_03_02;
// Java 프로그래밍 - 여러가지 연산자_2

public class Main {
    public static void main(String[] args) {

//      1. 비트 논리 연산자
        System.out.println(&quot;== 비트 논리 연산자 ==&quot;);
//      1-1. AND 연산자 (&amp;)
        System.out.println(&quot;== &amp; ==&quot;);

        int num1 = 5;
        int num2 = 3;

        int result = 0;
        result = num1 &amp; num2;
        System.out.println(&quot;result = &quot; + result);
        System.out.println(Integer.toBinaryString(num1));

        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(num1)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(num2)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(result)));

//      1-2. OR 연산자 (|)
        System.out.println(&quot;== | ==&quot;);

        result = num1 | num2 ;
        System.out.println(&quot;result = &quot; + result);
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(num1)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(num2)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(result)));


//      1-3. XOR 연산자 (^)
        System.out.println(&quot;== XOR ==&quot;);

        result = num1 ^ num2 ;
        System.out.println(&quot;result = &quot; + result);
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(num1)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(num2)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(result)));


//      1-4. 반전 연산자 (~)

        System.out.println(&quot;== ~ ==&quot;);

        result = ~num1;
        System.out.println(&quot;result = &quot; + result);
        System.out.printf(&quot;%s\n&quot;,Integer.toBinaryString(result));


//      2. 비트 이동 연산자
        System.out.println(&quot;== 비트 이동 연산자 ==&quot;);
//      2-1. &lt;&lt; 연산자

        int numA = 3;
        result = numA &lt;&lt;1;

        System.out.println(&quot;result = &quot; + result);
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(numA)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(result)));

//      2-2. &gt;&gt; 연산자
        result = numA &gt;&gt;1;

        System.out.println(&quot;result = &quot; + result);
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(numA)));
        System.out.printf(&quot;%04d\n&quot;,Integer.parseInt(Integer.toBinaryString(result)));



//      2-3. &gt;&gt;&gt; 연산자
        numA =-5;
        result = numA &gt;&gt;1;
        System.out.printf(&quot;%s\n&quot;,(Integer.toBinaryString(numA)));
        System.out.printf(&quot;%s\n&quot;,(Integer.toBinaryString(result)));

        result = numA &gt;&gt;&gt;1;
        System.out.printf(&quot;%s\n&quot;,(Integer.toBinaryString(numA)));
        System.out.printf(&quot;%s\n&quot;,(Integer.toBinaryString(result)));


    }

}
</code></pre>