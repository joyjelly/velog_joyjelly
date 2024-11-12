<h1 id="15컬렉션-프레임워크">15.컬렉션 프레임워크</h1>
<h2 id="1-컬렉션-프레임워크">1. 컬렉션 프레임워크</h2>
<h3 id="여러-데이터를-편리하게-관리-할-수-있게-만들어-놓은-것">여러 데이터를 편리하게 관리 할 수 있게 만들어 놓은 것.</h3>
<p>자료 구조 및 알고리즘을 구조화.</p>
<h3 id="대표-인터페이스">대표 인터페이스</h3>
<p>List 인터페이스, Set 인터페이스, Map 인터페이스</p>
<h2 id="2-list-인터페이스">2. List 인터페이스</h2>
<h3 id="순서가-있는-데이터의-집합">순서가 있는 데이터의 집합</h3>
<h3 id="데이터-중복-허용">데이터 중복 허용</h3>
<h3 id="대표-구현-클래스">대표 구현 클래스</h3>
<p>ArrayList, LinkedList, Vector </p>
<h2 id="3-set-인터페이스">3. Set 인터페이스</h2>
<h3 id="순서가-없는-데이터의-집합">순서가 없는 데이터의 집합</h3>
<h3 id="데이터의-중복-허용하지-않음">데이터의 중복 허용하지 않음</h3>
<h3 id="대표-구현-클래스-1">대표 구현 클래스</h3>
<p>HashSet, TreeSet</p>
<h2 id="4-map-인터페이스">4. Map 인터페이스</h2>
<p>키와 값의 쌍으로 이루어진 데이터 집합
순서를 유지하지 않음
대표 구현 클래스
HashMap, TreeMap</p>
<pre><code>package java_15;
// Practice
// 로또 번호 만들기

import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;

public class Practice {
    public static void main(String[] args) {
        HashSet&lt;Integer&gt; set = new HashSet&lt;&gt;();


        for (int i = 0;  set.size()&lt;6; i++) {
            int num = (int)(Math.random()*45)+1 ;
            set.add(num);
        }



        LinkedList&lt;Integer&gt; list = new LinkedList&lt;&gt;(set);
        Collections.sort(list);
        System.out.println(&quot;[로또번호] = &quot; + list);

    }
}
</code></pre>