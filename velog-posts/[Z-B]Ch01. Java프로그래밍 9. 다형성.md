<h1 id="9-다형성">9. 다형성</h1>
<h2 id="1-다형성">1. 다형성</h2>
<h3 id="한-객체가-여러가지-타입을-가질-수-있는-것">한 객체가 여러가지 타입을 가질 수 있는 것</h3>
<h3 id="부모클래스-타입의-참조변수로-자식클래스-인스턴스-참조">부모클래스 타입의 참조변수로 자식클래스 인스턴스 참조</h3>
<h2 id="2-instanceof">2. instanceof</h2>
<h3 id="실제-참조하고-있는-인스턴스의-타입-확인">실제 참조하고 있는 인스턴스의 타입 확인</h3>
<pre><code class="language-java">package java_09;
// Practice
// 아래의 클래스와 상속 관계에서 다형성을 이용하여
// Car 객체를 통해 아래와 같이 출력될 수 있도록 Test code 부분을 구현해보세요.
// 빵빵!
// 위이잉!
// 삐뽀삐뽀!

class Car {
    Car(){}
    public void horn() {
        System.out.println(&quot;빵빵!&quot;);
    }
}

class FireTruck extends Car {
    public void horn() {
        System.out.println(&quot;위이잉!&quot;);
    }
}

class Ambulance extends Car {
    public void horn() {
        System.out.println(&quot;삐뽀삐뽀!&quot;);
    }
}

public class Practice {
    public static void main(String[] args) {
        // Test code
        Car car = new Car();
        car.horn();

        car= new FireTruck();
        car.horn();

        car = new Ambulance();
        car.horn();

        Car car2[] = {new Car(),new FireTruck(),new Ambulance()};

        for (Car item : car2){
            item.horn();
        }


    }
}
</code></pre>