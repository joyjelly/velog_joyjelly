<h1 id="2-4-변수와-자료형">2-4. 변수와 자료형</h1>
<h2 id="1-자료형---리스트">1. 자료형 - 리스트</h2>
<ol>
<li><p>배열과 같이 여러 데이터를 담을 수 있는 자료형</p>
</li>
<li><p>추가로 여러가지 메소드를 제공</p>
<pre><code class="language-java">ArrayList l1 = new ArrayList();
l1.add(1);</code></pre>
</li>
<li><p>리스트 메소드
add , get, size, remove, clear, sort, contains</p>
<h2 id="2-자료형---맵">2. 자료형 - 맵</h2>
</li>
<li><p>key, value형태로 데이터를 저장하는 자료형</p>
</li>
<li><p>맵 메서드
put, get, size, remove, containsKey</p>
</li>
</ol>
<h2 id="3-자료형---제네릭스">3. 자료형 - 제네릭스</h2>
<ol>
<li><p>자료형을 명시적으로 지정</p>
</li>
<li><p>제한적일 수 있지만 안정성을 높여주고 형변환을 줄여줌</p>
</li>
</ol>
<pre><code class="language-java">package java_02_04.java_02_03;

// Java 프로그래밍 - 변수와 자료형_4

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {

//      1. 자료형 - 리스트

        System.out.println(&quot;== 리스트 ==&quot;);
    ArrayList l1 = new ArrayList();
//      1-1. add
        l1.add(1);
        l1.add(&quot;hello&quot;);
        l1.add(2);
        l1.add(3);
        l1.add(4);
        l1.add(&quot;world!&quot;);

        System.out.println(&quot;l1 = &quot; + l1);

        //0번 위치에 1을 넣는다!
        l1.add(0,1);
        System.out.println(&quot;l1 = &quot; + l1);



//      1-2. get
        System.out.println(&quot;l1.get(0) = &quot; + l1.get(0));
        System.out.println(&quot;l1.get(3) = &quot; + l1.get(3));

//      1-3. size
        System.out.println(&quot;l1.size() = &quot; + l1.size());
//      1-4. remove
        //해당 인덱스를 지운다
        l1.remove(0);
        System.out.println(&quot;l1 = &quot; + l1);
        //해당 값을 지운다
        l1.remove(Integer.valueOf(2));
        System.out.println(&quot;l1 = &quot; + l1);
//      1-5. clear
        l1.clear();
        System.out.println(&quot;l1 = &quot; + l1);

//      1-6. sort
        ArrayList l2 = new ArrayList();
        l2.add(5);
        l2.add(3);
        l2.add(4);

        System.out.println(&quot;l2 = &quot; + l2);

        //오름차순
        l2.sort(Comparator.naturalOrder());

        System.out.println(&quot;l2 오름차순= &quot; + l2);
        //내림차순
        l2.sort(Comparator.reverseOrder());
        System.out.println(&quot;l2 내림차순= &quot; + l2);

//      1-7. contains

        System.out.println(l2.contains(1));
        System.out.println(l2.contains(3));


//      2. Maps
        System.out.println(&quot;== Maps ==&quot;);

        HashMap map = new HashMap();



//      2-1. put
        map.put(&quot;kiwi&quot;,9000);
        map.put(&quot;apple&quot;,10000);
        map.put(&quot;mango&quot;,12000);
        System.out.println(&quot;map = &quot; + map);
//      2-2. get
        System.out.println(&quot;map.get(\&quot;mandarine\&quot;) = &quot; + map.get(&quot;mandarine&quot;));
        System.out.println(&quot;map.get(\&quot;kiwi\&quot;) = &quot; + map.get(&quot;kiwi&quot;));

//      2-3. size

        System.out.println(map.size());
//      2-4. remove

        System.out.println(map.remove(&quot;kiwi&quot;));
        System.out.println(map.remove(&quot;mandarine&quot;));
        System.out.println(&quot;map = &quot; + map);
//      2-5. containsKey

        System.out.println(map.containsKey(&quot;apple&quot;));
        System.out.println(map.containsKey(&quot;kiwi&quot;));


//      3. Generics
        System.out.println(&quot;== Generics ==&quot;);


        ArrayList l3 = new ArrayList();
        l3.add(1);
        l3.add(&quot;hello&quot;);
        System.out.println(&quot;l3 = &quot; + l3);

        ArrayList&lt;String&gt; l4 = new ArrayList&lt;&gt;();
        l4.add(&quot;hello&quot;);
        System.out.println(&quot;l4 = &quot; + l4);


        HashMap map1 = new HashMap();
        map1.put(123, &quot;id&quot;);
        map1.put(&quot;ad&quot;, 123);
        HashMap&lt;String,Integer&gt; map2 = new HashMap&lt;&gt;();

        map2.put(&quot;apple&quot;,1000);

        System.out.println(&quot;map1 = &quot; + map1);
        System.out.println(&quot;map2 = &quot; + map2);

    }

}
</code></pre>