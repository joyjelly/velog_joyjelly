<h1 id="12-내부클래스">12. 내부클래스</h1>
<h2 id="1-내부클래스-종류">1. 내부클래스 종류</h2>
<h3 id="내부클래스inner-class">내부클래스(Inner Class)</h3>
<h4 id="클래스-in-클래스-클래스-안에-선언-된-클래스">클래스 in 클래스 (클래스 안에 선언 된 클래스)</h4>
<pre><code>class Outer{
    class Inner{
    }
}</code></pre><h4 id="특징">특징</h4>
<p>내부클래스 에서 외부 클래스 멤버에 접근 가능
외부에서는 내부 클래스에 접근 불가.</p>
<h4 id="종류">종류</h4>
<p>인스턴스 클래스
정적 클래스
지역클래스
익명 클래스</p>
<h2 id="2-익명클래스">2. 익명클래스</h2>
<h3 id="1-이름을-가지지-않는-클래스">1. 이름을 가지지 않는 클래스</h3>
<h3 id="2-선언과-동시에-객체-생성">2. 선언과 동시에 객체 생성</h3>
<h3 id="3-일회용-클래스">3. 일회용 클래스</h3>
<pre><code>클래스 이름 참조변수 이름 = new  클래스 이름(){
...
};</code></pre><pre><code>package java_12;
// Java 프로그래밍 - 내부 클래스

//내부 클래스 구조
class Outer{
    public void print(){
        System.out.println(&quot;Outer.print&quot;);
    }

    class Inner{
        public void innerPrint(){
            Outer.this.print();
        }
    }

   static class InnerStaticClass{
        void innerPrint(){
            //Outer.this.print();
        }
    }
}
abstract class Person{
    public abstract void  printInfo();
}
class Student extends Person{
    @Override
    public void printInfo() {
        System.out.println(&quot;Student.printInfo&quot;);
    }
}

public class Main {

    public static void main(String[] args) {

//      외부 클래스
        Outer o1= new Outer();
//      내부 클래스 - 인스턴스
        Outer.Inner i1 = new Outer().new Inner();

//      내부 클래스 - 정적
        Outer.InnerStaticClass is1 = new Outer.InnerStaticClass();
//      익명 클래스
        Person p1 =new Person() {
            @Override
            public void printInfo() {
                System.out.println(&quot;Main.printInfo&quot;);
            }
        };

    }

}
</code></pre>