<p>ajax -&gt;success되면 추가된 결과를 보여줄 때, 페이지안의 값들을 지우고 추가하지 않는다면?
값들이 계속 쌓이게 된다.</p>
<p>이때 $(&quot;#아이디,비워야 할 리스트의 상위 요소&quot;).empty()를 한다.</p>
<p>예시 :</p>
<pre><code class="language-javascript">success: function(jsonObj) {
              $(&quot;#output&quot;).empty();
              var output =&quot;&quot;;</code></pre>
<pre><code class="language-html">&lt;table&gt;
&lt;thead&gt;
&lt;tr&gt;
&lt;th&gt;NO&lt;/th&gt;
&lt;th &quot;&gt;&lt;a&gt;공지사항 제목&lt;/a&gt;&lt;/th&gt;
&lt;th&gt;&lt;a&gt;게시 날짜&lt;/a&gt;&lt;/th&gt;
&lt;th&gt;&lt;a&gt;게시글 상태&lt;/a&gt;&lt;/th&gt;
&lt;/tr&gt;
&lt;/thead&gt;
&lt;tbody id =&quot;output&quot;&gt;</code></pre>