<h1 id="2-2-변수와-자료형">2-2. 변수와 자료형</h1>
<h2 id="1-자료형">1. 자료형</h2>
<ol>
<li>변수의 종류, 단위</li>
</ol>
<ul>
<li>숫자</li>
<li>불린</li>
<li>문자</li>
<li>문자열
...</li>
</ul>
<ol start="2">
<li>변수의 종류에 따라 담을 수 있는 데이터 타입과 크기가 다르다.</li>
</ol>
<h2 id="2-자료형---숫자">2. 자료형 - 숫자</h2>
<ol>
<li>숫자형태의 자료형</li>
</ol>
<ul>
<li>정수 / 실수 / 2진수, 8진수, 16진수</li>
</ul>
<h2 id="3-자료형---불린">3. 자료형 - 불린</h2>
<ol>
<li>참과 거짓을 나타내는 자료형</li>
</ol>
<h2 id="4-자료형---문자">4. 자료형 - 문자</h2>
<ol>
<li>한개의 문자 표현에 사용하는 자료형</li>
</ol>
<pre><code class="language-java">package java_02_2;

// Java 프로그래밍 - 변수와 자료형_2

public class Main {
    public static void main(String[] args) {

//      1. 자료형 - 숫자
        System.out.println(&quot;== 숫자 ==&quot;);
//      1-1. 정수

        int intNum = 10;

        System.out.println(&quot;intNum = &quot; + intNum);

        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);


        int intNum2 = Integer.MAX_VALUE+1;
        System.out.println(&quot;intNum2 = &quot; + intNum2);
        long longNum = (long)Integer.MAX_VALUE +1;
        System.out.println(&quot;longNum = &quot; + longNum);

//      1-2. 실수
    float floatNum = 1.23f;
    double doubleNum = 1.23;
        System.out.println(&quot;floatNum = &quot; + floatNum);
        System.out.println(&quot;doubleNum = &quot; + doubleNum);

        System.out.println(Float.MAX_VALUE);
        System.out.println(Double.MAX_VALUE);


//      1-3. 2진수 / 8진수 / 16진수
    int numBase2 = 0b1100;
        System.out.println(&quot;numBase2 = &quot; + numBase2);
        int numBase8 = 014;
        System.out.println(&quot;numBase8 = &quot; + numBase8);
        int numBase16 = 0xC;
        System.out.println(&quot;numBase16 = &quot; + numBase16);

        System.out.println(&quot;0b&quot;+ Integer.toBinaryString(numBase2));
        System.out.println(&quot;0b&quot;+ Integer.toOctalString(numBase8));
        System.out.println(&quot;0b&quot;+ Integer.toHexString(numBase16));
//      2. 자료형 - 부울
        System.out.println(&quot;== 부울 ==&quot;);

        boolean isPass = true;
        boolean isOk = false;

        System.out.println(&quot;isOk = &quot; + isOk);
        System.out.println(&quot;isPass = &quot; + isPass);
//      3. 자료형 - 문자
        System.out.println(&quot;== 문자 ==&quot;);
        char keyFirst = 'a';
        System.out.println(&quot;keyFirst = &quot; + keyFirst);
        System.out.println((int)keyFirst);

    }
}
</code></pre>