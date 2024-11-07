<h1 id="6-다차원-배열">6. 다차원 배열</h1>
<h2 id="1-다차원-배열">1. 다차원 배열</h2>
<h3 id="일차원-배열">일차원 배열</h3>
<pre><code class="language-java">int[] myArray1 = {1,2,3,4,5};
char[] myArray2 = {'a','b','c','d'};</code></pre>
<h3 id="다차원-배열">다차원 배열</h3>
<pre><code class="language-java">int[][] myArray3 = {{1,2,3},{4,5,6}};
int[][][] myArray4 = {{{1,2},{3,4}},{{5,6},{7,8}}};</code></pre>
<h2 id="2-이차원-배열">2. 이차원 배열</h2>
<h3 id="이차원-배열의-생성방법">이차원 배열의 생성방법</h3>
<pre><code class="language-java">int[][] myArray = {{1,2,3},{4,5,6}};
int[][] myArray2 = new int[2][3]; //[행][열]</code></pre>
<pre><code class="language-java">package java_06;
// Java 프로그래밍 - 다차원 배열

public class Main {
    public static void main(String[] args) {

        // 1. 일차원 배열
        System.out.println(&quot;== 일차원 배열 ==&quot;);
        int[] myArray = {1,2,3};
        for(int temp : myArray){
            System.out.println(temp);
        }



        // 2. 이차원 배열
        System.out.println(&quot;== 이차원 배열 ==&quot;);
        int[][] myArray2 = {{1,2,3},{4,5,6}};
        System.out.println(&quot;myArray2[1][2] = &quot; + myArray2[1][2]);

        for (int i = 0; i &lt; myArray2.length; i++) {
            for (int j = 0; j &lt; myArray2[i].length; j++) {
                System.out.println(myArray2[i][j]);
            }
        }

        for (int[] ints: myArray2){
            for (int asInt : ints){
                System.out.println(&quot;asInt = &quot; + asInt);
            }
        }

//      Q1. 아래와 같이 3x3 행렬이 2차원 배열로 초기화 되어있다.
//          모든 원소를 1로 변경하고, 대각 원소는 10으로 변경하시오.
        int [][] testArray1 = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        for (int i = 0; i &lt; testArray1.length; i++) {
            for (int j = 0; j &lt; testArray1[i].length; j++) {
                if (i==j){

                    testArray1[i][j]=10;
                }else {

                    testArray1[i][j]=1;
                }

            }
        }
        for (int i = 0; i &lt; testArray1.length; i++) {
            for (int j = 0; j &lt; testArray1[i].length; j++) {
                System.out.println(&quot;testArray1[i][j] = &quot; + testArray1[i][j]);
            }
        }
    }
}
</code></pre>