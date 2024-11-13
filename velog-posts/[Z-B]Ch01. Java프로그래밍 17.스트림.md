<h1 id="17스트림">17.스트림</h1>
<h2 id="1-스트림">1. 스트림</h2>
<p>배열 ,컬렉션 등의 데이터를 하나씩 참조하여 처리 가능한 기능
for문의 사용을 줄여 코드를 간결하게 함.</p>
<h3 id="스트림의-3가지-구성">스트림의 3가지 구성</h3>
<ul>
<li>스트림 생성</li>
<li>중개연산</li>
<li>최종연산</li>
</ul>
<pre><code>데이터 소스 객체. stream 생성().중개연산().최종연산();</code></pre><h2 id="2-스트림-생성">2. 스트림 생성</h2>
<h3 id="배열스트림">배열스트림</h3>
<pre><code>String[] arr = new String[]{&quot;a&quot;,&quot;b&quot;,&quot;c&quot;};
Stream stream = Arrays.stream(arr);</code></pre><h3 id="컬렉션-스트림">컬렉션 스트림</h3>
<pre><code>Stream stream = list.stream();</code></pre><h2 id="3-스트림-중개연산">3. 스트림 중개연산</h2>
<h3 id="filtering">filtering</h3>
<ul>
<li>필터 내부 조건에 참인 요소들을 추출</li>
</ul>
<h3 id="mapping">Mapping</h3>
<ul>
<li>map 안의 연산을 요소별로 수행<pre><code>IntStream intStream = IntStream.range(1,10).map(n-&gt;n+1);</code></pre></li>
<li><blockquote>
<p>1<del>10에서 2</del>11까지 변환된다!</p>
</blockquote>
</li>
</ul>
<h2 id="4-스트림-최종연산">4. 스트림 최종연산</h2>
<p>결과값을 낸다</p>
<h3 id="sumaverage">Sum,Average</h3>
<pre><code>IntStream.range(1,5).sum()
IntStream.range(1,5).average().getAsDouble()</code></pre><h3 id="minmax">min,max</h3>