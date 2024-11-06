<h1 id="2-3변수와-자료형">2-3.변수와 자료형</h1>
<h2 id="1-자료형---문자열">1. 자료형 - 문자열</h2>
<ol>
<li><p>문자들로 이루어진 집합</p>
<pre><code class="language-java">String s1 = &quot;Hello World!&quot;;
String s2 = &quot;01234&quot;;</code></pre>
</li>
<li><p>문자열 메소드</p>
</li>
</ol>
<ul>
<li>equals, indexOf, replace, substring... 등</li>
</ul>
<h2 id="2-자료형---stringbuffer">2. 자료형 - StringBuffer</h2>
<ol>
<li>문자열을 자주 추가하거나 변경 할 때 사용하는 자료형</li>
</ol>
<pre><code class="language-java">StringBuffer sb1 = new StringBuffer(&quot;Hello World!&quot;);</code></pre>
<p>2.StringBuffer 메소드</p>
<ul>
<li>append , insert, substring</li>
</ul>
<h2 id="3-자료형---배열">3. 자료형 - 배열</h2>
<ol>
<li>많은 수의 데이터를 담을 수 있는 자료형<pre><code class="language-java">int[] myArray1 = {1,2,3,4,5};
char[] myArray2 = {'a','b','c','d'};</code></pre>
</li>
</ol>
<pre><code class="language-java">package java_02_03;

// Java 프로그래밍 - 변수와 자료형_3

import java.util.Locale;

public class Main {
    public static void main(String[] args) {

//      1. 자료형 - 문자열
        System.out.println(&quot;== 문자열 ==&quot;);
        String s1 = &quot;Hello World&quot;;
        String s2 = &quot;01234&quot;;

        System.out.println(&quot;s1 = &quot; + s1);
        System.out.println(&quot;s2 = &quot; + s2);


//      1-1. equals
        String s3 = &quot;Hi&quot;;
        String s4 = &quot;Hi&quot;;
        System.out.println(s3.equals(s4));
        System.out.println(s3==s4);
        String s5 = new String(&quot;Hi&quot;);
        System.out.println(s3.equals(s5));

        //비교연산자는 다르다고 나옴!
        System.out.println(s3==s5);
        //보통 equals사용
//      1-2. indexOf
        //특정 문자열의 위치
        String s6 = &quot;Hello! World!&quot;;
        System.out.println(s6.indexOf(&quot;!&quot;));
        //처음느낌표 -&gt; 다음의 느낌표를 찾아라!
        System.out.println(s6.indexOf(&quot;!&quot;,s6.indexOf(&quot;!&quot;)+1));

//      1-3. replace
        String s7 = s6.replace(&quot;Hello&quot;, &quot;Bye&quot;);
        System.out.println(s7);

//      1-4. substring
        //3번 제외하고 0,1,2
        System.out.println(s7.substring(0,3));
        //느낌표까지!
        System.out.println(s7.substring(0,s7.indexOf(&quot;!&quot;)+1));

//      1-5. toUpperCase
        System.out.println(s7.toUpperCase());


//      2. 자료형 - StringBuffer
        System.out.println(&quot;== StringBuffer ==&quot;);
        StringBuffer sb1 = new StringBuffer();
        sb1.append(&quot;01234&quot;);
        System.out.println(&quot;sb1 = &quot; + sb1);
        sb1.append(&quot;56789&quot;);
        System.out.println(&quot;sb1 = &quot; + sb1);


        String a = &quot;01234&quot;;
        String b = &quot;56789&quot;;
        String bak = a;
        System.out.println(a==bak);

        a +=b;
        System.out.println(a);
        System.out.println(a==bak);





//      3. 자료형 - 배열
        System.out.println(&quot;== 배열 ==&quot;);


        int[] myArray1 ={1,2,3,4,5};
        System.out.println(myArray1[0]);
        System.out.println(myArray1[1]);
        System.out.println(myArray1[2]);
        System.out.println(myArray1[3]);
        System.out.println(myArray1[4]);

        char[] myArray2 = {'a','b','c'};
        System.out.println(myArray2[2]);

        String[] myArray3 = new String[3];
        myArray3[0] = &quot;Hello&quot;;
        myArray3[1] = &quot; &quot;;
        myArray3[2] = &quot;World!&quot;;
        System.out.println(myArray3[0]+myArray3[1]+myArray3[2]);



    }
}

</code></pre>