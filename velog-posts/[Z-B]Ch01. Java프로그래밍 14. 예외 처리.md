<h1 id="14-예외처리">14. 예외처리</h1>
<h2 id="1-예외">1. 예외</h2>
<h3 id="정상적이지-않은-case">정상적이지 않은 Case</h3>
<ul>
<li>0으로 나누기</li>
<li>배열의 인덱스 초과</li>
<li>없는 파일 열기 
...</li>
</ul>
<h2 id="2-예외처리">2. 예외처리</h2>
<h3 id="정상적이지-않은-case에-대한-적절한-처리-방법">정상적이지 않은 Case에 대한 적절한 처리 방법</h3>
<pre><code class="language-java">try{

}catch (예외 case 1){

}catch(예외 case 2){

}
int a = 0;

try{
a = 5/0;
}catch (~~){
sout e

}

</code></pre>
<h2 id="3-finally">3. finally</h2>
<p>예외 발생 여부와 관계없이 항상 실행되는 부분.</p>
<pre><code>try{
예외가 발생 할 수도 있는 부분
}catch (예외 1){

}finally{
항상 실행되는 부분
}
</code></pre><h2 id="4-throw-throws">4. throw, throws</h2>
<p>throw : 예외를 발생시킴.
-&gt;강제적으로</p>
<p>throws : 예외를 전가시킴.
-&gt;다른 매서드로 옮겨감</p>