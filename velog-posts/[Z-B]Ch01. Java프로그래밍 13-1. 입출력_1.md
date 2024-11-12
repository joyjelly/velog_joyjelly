<h1 id="13-1-입출력_1">13-1. 입출력_1</h1>
<h2 id="1-콘솔-입력">1. 콘솔 입력</h2>
<p>입출력 방식 중 콘솔 입력방법</p>
<pre><code>System.in.read()
InputStreamReader reader = ...
BufferedReader br = ...
Scanner ...</code></pre><h2 id="2-콘솔-출력">2. 콘솔 출력</h2>
<p>입출력 방식 중 콘솔 출력 방법</p>
<pre><code>System.out.println();
System.out.print();
System.out.printf();</code></pre><pre><code>package java_13_1;
// Java 프로그래밍 - 입출력_1

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

    public static void referInputStream() throws IOException {
//      System.in
//        System.out.println(&quot;== System.in ==&quot;);
//        System.out.print(&quot;입력 : &quot;);
//        int a = System.in.read() -'0';
//        System.out.println(&quot;a = &quot; + a);
//        //남아있는 데이터 소진
//        System.in.read(new byte[System.in.available()]);



//      InputStreamReader
//        System.out.println(&quot;== InputStreamReader ==&quot;);
//        InputStreamReader reader = new InputStreamReader(System.in);
//        char[] c = new char[3];
//        System.out.print(&quot;입력 : &quot;);
//        reader.read(c);
//        System.out.println(c);

//      BufferedReader
        System.out.println(&quot;== BufferedReader ==&quot;);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print(&quot;입력 : &quot;);
        String s1 = br.readLine();
        System.out.println(&quot;s1 = &quot; + s1);


    }

    public static void main(String[] args) throws IOException {

//      1. 입력
//      1-1. 다른 입력 방식 참고
   //     referInputStream();

//      1-2. Scanner
        System.out.println(&quot;== Scanner ==&quot;);
        Scanner sc = new Scanner(System.in);
//        System.out.print(&quot;입력 1 : &quot;);
//        System.out.println(sc.next());
//        sc.nextLine();
//
//        System.out.print(&quot;입력 2: &quot;);
//        System.out.println(sc.nextInt());
//        sc.nextLine();
//
//        System.out.print(&quot;입력 3: &quot;);
//        System.out.println(sc.nextLine());


//      참고) 정수, 문자열 변환
        int num = Integer.parseInt(&quot;1234&quot;);
        String string = Integer.toString(12345);



//      2. 출력
        System.out.println(&quot;== 출력 ==&quot;);

        System.out.println(&quot;Hello&quot;);
        System.out.println(&quot;World&quot;);

        System.out.print(&quot;Hello&quot;);
        System.out.print(&quot;World&quot;);
        System.out.println();

        System.out.printf(&quot;Hello&quot;);
        System.out.printf(&quot;World&quot;);
        System.out.println();


        String s = &quot;자바&quot;;
        int number = 3;

        System.out.println(s+&quot;는 언어선호도 &quot;+number+&quot;위 입니다&quot;);
        System.out.printf(&quot;%s는 언어 선호도  %d 위 입니다.\n&quot; , s , number);

        System.out.printf(&quot;%d\n&quot;,10);
        System.out.printf(&quot;%o\n&quot;,10);
        System.out.printf(&quot;%x\n&quot;,10);
        System.out.printf(&quot;%f\n&quot;,5.2f);
        System.out.printf(&quot;%c\n&quot;,'A'); //문자
        System.out.printf(&quot;%s\n&quot;,&quot;안녕하세욘&quot;);//문자열

        System.out.printf(&quot;%5d\n&quot;,123);
        System.out.printf(&quot;%5d\n&quot;,1234);
        System.out.printf(&quot;%5d\n&quot;,12345);

        System.out.printf(&quot;%-5d\n&quot;,123);

        System.out.printf(&quot;%.2f\n&quot;,1.238465);//반올림해서 출력 -&gt;1.24


    }
}

</code></pre>