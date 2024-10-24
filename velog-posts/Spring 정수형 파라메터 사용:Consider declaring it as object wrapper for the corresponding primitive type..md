<p>파라메터 값이 null 일 때
-&gt; 정수형 값으로 받는다면 int 타입은 null을 저장 할 수 없기때문에 오류가 발생한다!
(요청 정보의 헤더에서 해당 파라메터를 찾는데, 주소창에 쿼리스트링이 없다? 해당 파라메터 = null)</p>
<blockquote>
</blockquote>
<p>Consider declaring it as object wrapper for the corresponding primitive type.</p>
<p>int는 ㄴㄴ 니까 Wrapper인 Integer로 써라!임</p>