#encoding=utf8
from trans.utils.base import SiteRequestHandler

class Counts(SiteRequestHandler):
	def GET(self, book='', chapterIdx=''):
		self.write('[[0,16],[1,4],[2,4],[3,5],[4,3],[5,3],[8,1],[10,1],[12,1],[13,2],[16,1],[17,2],[20,2],[22,1],[26,2],[29,4],[33,3],[44,2],[45,2],[48,3],[56,1],[57,2],[64,2],[68,5],]')

class AjaxComments(SiteRequestHandler):
	def GET(self, book='', chapterIdx=''):
		self.write('''
<li class="comment" id="3"><dl><dt><a href="" rel="nofollow">
						sofring
						</a><span class="meta">2009-10-20 13:58:24</span></dt><dd><p>介绍的“绍”字达成繁体了咯，貌似字体没有第一版好看呀</p></dd></dl></li>

<li class="comment" id="6"><dl><dt><a href="" rel="nofollow">
						mitnk
						</a><span class="meta">2009-10-21 10:17:00</span></dt><dd><p>如果你装有微软Yehei字体的话，看到的就是Yehei了。挺好看的字体。</p></dd></dl></li>

<li class="comment" id="8"><dl><dt><a href="" rel="nofollow">
						sofring
						</a><span class="meta">2009-10-22 13:10:13</span></dt><dd><p>是雅黑呀，不过“绍”字确实写成繁体了吧？</p></dd></dl></li>

<li class="comment" id="95"><dl><dt><a href="" rel="nofollow">
						
						</a><span class="meta">2010-02-05 15:01:26</span></dt><dd><p></p></dd></dl></li>

<li class="comment" id="398"><dl><dt><a href="" rel="nofollow">
						
						</a><span class="meta">2010-11-15 16:08:10</span></dt><dd><p>Good book</p></dd></dl></li>

<li class="comment" id="401"><dl><dt><a href="789.com" rel="nofollow">
						Gook
						</a><span class="meta">2010-11-16 16:13:04</span></dt><dd><p>This is a good book</p></dd></dl></li>

<li class="comment" id="409"><dl><dt><a href="" rel="nofollow">
						name
						</a><span class="meta">2010-11-22 15:33:21</span></dt><dd><p>This is a good book</p></dd></dl></li>

<li class="comment" id="410"><dl><dt><a href="" rel="nofollow">
						namenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamename
						</a><span class="meta">2010-11-22 16:37:46</span></dt><dd><p>This is a good book</p></dd></dl></li>

<li class="comment" id="803"><dl><dt><a href="ngloom.me" rel="nofollow">
						
						</a><span class="meta">2011-06-05 10:58:25</span></dt><dd><p>thanks for the great work. </p></dd></dl></li>

<li class="comment" id="828"><dl><dt><a href="" rel="nofollow">
						xinguo
						</a><span class="meta">2011-06-18 11:44:24</span></dt><dd><p>错误百出，误人子弟。</p></dd></dl></li>

<li class="comment" id="930"><dl><dt><a href="http://lilydjwg.is-programmer.com/" rel="nofollow">
						依云
						</a><span class="meta">2011-08-22 17:40:13</span></dt><dd><p>显示评注时下方显示“正在装载注释”</p></dd></dl></li>

<li class="comment" id="949"><dl><dt><a href="www.cyrec.org" rel="nofollow">
						Cyrec
						</a><span class="meta">2011-08-28 19:39:21</span></dt><dd><p>怎么都在抠字眼...</p></dd></dl></li>

<li class="comment" id="951"><dl><dt><a href="" rel="nofollow">
						
						</a><span class="meta">2011-08-30 10:02:49</span></dt><dd><p></p></dd></dl></li>

<li class="comment" id="1151"><dl><dt><a href="http://www.ngloom.me" rel="nofollow">
						NGloom
						</a><span class="meta">2011-12-04 23:14:52</span></dt><dd><p>great work,
感谢你们的工作~ 
</p></dd></dl></li>

<li class="comment" id="1565"><dl><dt><a href="" rel="nofollow">
						liuxiaoyu
						</a><span class="meta">2012-05-29 23:12:43</span></dt><dd><p>这个评论好牛逼！！！我喜欢这个！！以前一直想做来着！！！</p></dd></dl></li>

<li class="comment" id="1572"><dl><dt><a href="" rel="nofollow">
						cacsgr
						</a><span class="meta">2012-06-08 07:54:14</span></dt><dd><p>牛！</p></dd></dl></li>


			''')
class AjaxComment(SiteRequestHandler):
	def GET(self, book='', chapterIdx='', commentIdx=''):
		self.write('''

<li class="comment" id="3"><dl><dt><a href="" rel="nofollow">
						sofring
						</a><span class="meta">2009-10-20 13:58:24</span></dt><dd><p>介绍的“绍”字达成繁体了咯，貌似字体没有第一版好看呀</p></dd></dl></li>

<li class="comment" id="6"><dl><dt><a href="" rel="nofollow">
						mitnk
						</a><span class="meta">2009-10-21 10:17:00</span></dt><dd><p>如果你装有微软Yehei字体的话，看到的就是Yehei了。挺好看的字体。</p></dd></dl></li>

<li class="comment" id="8"><dl><dt><a href="" rel="nofollow">
						sofring
						</a><span class="meta">2009-10-22 13:10:13</span></dt><dd><p>是雅黑呀，不过“绍”字确实写成繁体了吧？</p></dd></dl></li>

<li class="comment" id="95"><dl><dt><a href="" rel="nofollow">
						
						</a><span class="meta">2010-02-05 15:01:26</span></dt><dd><p></p></dd></dl></li>

			''')