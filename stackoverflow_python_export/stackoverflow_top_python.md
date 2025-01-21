# Most Voted Python Questions on Stack Overflow

*Generated on: 2025-01-21 12:59:28*

## 1. What does the &quot;yield&quot; keyword do in Python?

**Vote count:** 13033
**Views:** 3419836
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)

### Question

<p>What functionality does the <a href="https://docs.python.org/3/reference/simple_stmts.html#yield" rel="noreferrer"><code>yield</code></a> keyword in Python provide?</p>
<p>For example, I'm trying to understand this code<sup><strong>1</strong></sup>:</p>
<pre><code>def _get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist &lt; self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist &gt;= self._median:
        yield self._rightchild  
</code></pre>
<p>And this is the caller:</p>
<pre><code>result, candidates = [], [self]
while candidates:
    node = candidates.pop()
    distance = node._get_dist(obj)
    if distance &lt;= max_dist and distance &gt;= min_dist:
        result.extend(node._values)
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
return result
</code></pre>
<p>What happens when the method <code>_get_child_candidates</code> is called?
Is a list returned? A single element? Is it called again? When will subsequent calls stop?</p>

<hr />
<sub>
1. This piece of code was written by Jochen Schulz (jrschulz), who made a great Python library for metric spaces. This is the link to the complete source: <a href="https://well-adjusted.de/~jrspieker/mspace/" rel="noreferrer">Module mspace</a>.</sub> 


---

## 2. What does if __name__ == &quot;__main__&quot;: do?

**Vote count:** 8338
**Views:** 4825982
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

### Question

<p>What does this do, and why should one include the <code>if</code> statement?</p>
<pre class="lang-py prettyprint-override"><code>if __name__ == &quot;__main__&quot;:
    print(&quot;Hello, World!&quot;)
</code></pre>
<hr />
<p><sub>If you are trying to close a question where someone should be using this idiom and isn't, consider closing as a duplicate of <a href="https://stackoverflow.com/questions/6523791">Why is Python running my module when I import it, and how do I stop it?</a> instead. For questions where someone simply hasn't called any functions, or incorrectly expects a function named <code>main</code> to be used as an entry point automatically, use <a href="https://stackoverflow.com/questions/17257631">Why doesn&#39;t the main() function run when I start a Python script? Where does the script start running?</a>.</sub></p>


---

## 3. Does Python have a ternary conditional operator?

**Vote count:** 8033
**Views:** 3031106
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator)

### Question

<p>Is there a <a href="https://en.wikipedia.org/wiki/%3F:#Python" rel="noreferrer">ternary conditional operator</a> in Python?</p>


---

## 4. What are metaclasses in Python?

**Vote count:** 7460
**Views:** 1216436
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)

### Question

<p>What are <a href="https://docs.python.org/3/reference/datamodel.html#metaclasses" rel="noreferrer">metaclasses</a>? What are they used for?</p>


---

## 5. How do I check whether a file exists without exceptions?

**Vote count:** 7264
**Views:** 5809017
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions)

### Question

<p>How do I check whether a file exists or not, without using the <a href="https://docs.python.org/3.6/reference/compound_stmts.html#try" rel="noreferrer"><code>try</code></a> statement?</p>


---

## 6. How do I merge two dictionaries in a single expression in Python?

**Vote count:** 7065
**Views:** 3513756
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python)

### Question

<p>I want to merge two dictionaries into a new dictionary.</p>
<pre><code>x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = merge(x, y)

&gt;&gt;&gt; z
{'a': 1, 'b': 3, 'c': 4}
</code></pre>
<p>Whenever a key <code>k</code> is present in both dictionaries, only the value <code>y[k]</code> should be kept.</p>


---

## 7. How do I execute a program or call a system command?

**Vote count:** 6235
**Views:** 5011019
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command)

### Question

<p>How do I call an external command within Python as if I had typed it in a shell or command prompt?</p>


---

## 8. How do I create a directory, and any missing parent directories?

**Vote count:** 5767
**Views:** 3908813
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories)

### Question

<p>How do I create a directory at a given path, and also create any missing parent directories along that path? For example, the Bash command <code>mkdir -p /path/to/nested/directory</code> does this.</p>


---

## 9. How to access the index value in a &#39;for&#39; loop?

**Vote count:** 5589
**Views:** 4797820
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop)

### Question

<p>How do I access the index while iterating over a sequence with a <code>for</code> loop?</p>
<pre class="lang-py prettyprint-override"><code>xs = [8, 23, 45]

for x in xs:
    print(&quot;item #{} = {}&quot;.format(index, x))
</code></pre>
<p>Desired output:</p>
<pre class="lang-none prettyprint-override"><code>item #1 = 8
item #2 = 23
item #3 = 45
</code></pre>


---

## 10. How do I make a flat list out of a list of lists?

**Vote count:** 5443
**Views:** 4507685
**Question link:** [Stack Overflow](https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists)

### Question

<p>I have a list of lists like</p>
<pre><code>[
    [1, 2, 3],
    [4, 5, 6],
    [7],
    [8, 9]
]
</code></pre>
<p>How can I flatten it to get <code>[1, 2, 3, 4, 5, 6, 7, 8, 9]</code>?</p>
<hr />
<p><sub>If your list of lists comes from a nested list comprehension, the problem can be solved more simply/directly by fixing the comprehension; please see <a href="https://stackoverflow.com/questions/1077015">How can I get a flat result from a list comprehension instead of a nested list?</a>.</sub></p>
<p><sub>The most popular solutions here generally only flatten one &quot;level&quot; of the nested list. See <a href="https://stackoverflow.com/questions/2158395">Flatten an irregular (arbitrarily nested) list of lists</a> for solutions that completely flatten a deeply nested structure (recursively, in general).</sub></p>


---

