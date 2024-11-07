<h1 id="7-1클래스와-객체">7-1.클래스와 객체</h1>
<h2 id="1-클래스">1. 클래스</h2>
<h3 id="객체를-정의하는-설계도">객체를 정의하는 설계도</h3>
<p>-&gt; 자동차에 대해 정의된 설계도(디자인, 무게, 가격,,,,브레이크,,,)
-&gt; 차1,차2...가 나옴(기능과 특징을 실체화)</p>
<h3 id="붕어빵-틀">붕어빵 틀</h3>
<p>-&gt; 슈붕 팥붕...</p>
<h3 id="레시피">레시피</h3>
<p>-&gt; 요리1,요리2...</p>
<h2 id="2-객체-인스턴스">2. 객체, 인스턴스</h2>
<h3 id="객체">객체</h3>
<p>실체</p>
<h3 id="인스턴스">인스턴스</h3>
<p>클래스와 객체의 관계
클래스로부터 객체를 선언 (인스턴스화)
 -&gt; 어떤 객체는 어떤 클래스의 인스턴스</p>
<h3 id="클래스-사용">클래스 사용</h3>
<h4 id="클래스--객체를-만들기-위한-설계도">클래스 : 객체를 만들기 위한 설계도</h4>
<p>객체변수 + 매서드로 이루어져있다.</p>
<pre><code class="language-java">public class 클래스명 {
//객체변수
//매서드
-&gt; 리턴타입 매서드명 (파라메터){기능}
//접근제어자
//static
}
클래스명 객체명 = new 클래스명 ();</code></pre>
<h2 id="3-생성자">3. 생성자</h2>
<h3 id="객체가-생성될-때-자동으로-호출됨">객체가 생성될 때 자동으로 호출됨</h3>
<h3 id="생성자-규칙">생성자 규칙</h3>
<ol>
<li>클래스명과 이름 맞추기</li>
<li>리턴타입 없음<pre><code class="language-java">public class 클래스명 {
 클래스명(){} -&gt;생성자
}</code></pre>
</li>
</ol>
<h2 id="4-this-this">4. this, this()</h2>
<h3 id="this">this</h3>
<p>객체 자신을 의미한다</p>
<h3 id="this-1">this()</h3>
<p>생성자</p>
<pre><code class="language-java">package java_07;
// Java 프로그래밍 - 클래스와 객체_1

// Car 클래스 - 객체변수, 메소드
class Car{
    String name;
    String type;

   public Car(){

    }

    public void printCarInfo(){
        System.out.println(&quot;==car info==&quot;);
        System.out.println(&quot;name = &quot; + name);
        System.out.println(&quot;type = &quot; + type);
    }

    public void move(){
        System.out.println(&quot;이동!&quot;);
    }

    public void breake(){
        System.out.println(&quot;정지!&quot;);
    }
}

// Car2 클래스 - 생성자, this
class Car2{
    String name;
    String type;

    public Car2(String name, String type){
        this.name = name;
        this.type = name;
        System.out.println(&quot;생성자 출력!&quot;);
    }

    public void printCarInfo(){
        System.out.println(&quot;==car info==&quot;);
        System.out.println(&quot;name = &quot; + name);
        System.out.println(&quot;type = &quot; + type);
    }
    public void load(){
        System.out.println(&quot;짐을 주세용&quot;);
    }
    public void horn(){
        System.out.println(&quot;빵빵&quot;);
    }

}

public class Main {

    public static void main(String[] args) {
//      Car 클래스 사용
    Car car = new Car();
    car.name = &quot;a&quot;;
    car.type =&quot;suv&quot;;

    car.printCarInfo();
    car.breake();
    car.move();

//      Car2 클래스 사용
    Car2 car2 = new Car2(&quot;b&quot;,&quot;sedan&quot;);

    car2.printCarInfo();
    car2.load();
    car2.horn();

    }
}
</code></pre>