(function(){var c={id:"b72113a7702cfc915d773f5432b147cf",dm:["djangobook.py3k.cn"],etrk:[],js:"tongji.baidu.com/hm-web/js/",icon:'/hmt/icon/21|gif|20|20',br:false,ctrk:false,align:-1,nv:-1,vdur:1800000,age:31536000000,se:[[1,'baidu.com','word|wd',1,'news,tieba,zhidao,mp3,image,video,hi,baike,wenku,opendata,jingyan'],[2,'google.com','q',0,'tbm=isch,tbm=vid,tbm=nws|source=newssearch,tbm=blg'],[3,'google.cn','q',0,''],[4,'sogou.com','query',1,'news,mp3,pic,v,zhishi,blogsearch'],[5,'zhongsou.com','w',1,'p,z,gouwu,bbs,mp3'],[6,'search.yahoo.com','p',1,'news,images,video'],[7,'one.cn.yahoo.com','p',1,'news,image,music'],[8,'soso.com','w',1,'image,video,music,sobar,wenwen,news,life,baike,blog'],[9,'114search.118114.cn','kw',0,''],[10,'search.live.com','q',0,''],[11,'youdao.com','q',1,'image,news,gouwu,mp3,video,blog,reader'],[12,'gougou.com','search',1,'movie,mp3,book,soft,game'],[13,'bing.com','q',2,'images,videos,news']]};var g=true,h=null;function j(a,b){if(window.sessionStorage)try{window.sessionStorage.setItem(a,b)}catch(d){}}function l(a){return window.sessionStorage?window.sessionStorage.getItem(a):h};function m(a,b){var d=a.match(RegExp("(^|&|\\?|#)("+b+")=([^&#]*)(&|$|#)",""));return d?d[3]:h}function n(a){var b;return(b=(a=a.match(/^(https?:\/\/)?([^\/\?#]*)/))?a[2].replace(/.*@/,""):h,a=b)?a.replace(/:\d+$/,""):a};var o=navigator.cookieEnabled,p=navigator.javaEnabled(),q=navigator.language||navigator.browserLanguage||navigator.systemLanguage||navigator.userLanguage||"",r=window.screen.width+"x"+window.screen.height,s=window.screen.colorDepth;function t(a,b){var d=new Image,e="mini_tangram_log_"+Math.floor(Math.random()*2147483648).toString(36);window[e]=d;d.onload=d.onerror=d.onabort=function(){d.onload=d.onerror=d.onabort=h;d=window[e]=h;b&&b(a)};d.src=a};function u(a,b,d){a.attachEvent?a.attachEvent("on"+b,function(b){d.call(a,b)}):a.addEventListener&&a.addEventListener(b,d,false)};var v;function w(){if(!v)try{v=document.createElement("input"),v.type="hidden",v.style.display="none",v.addBehavior("#default#userData"),document.getElementsByTagName("head")[0].appendChild(v)}catch(a){return false}return g};var x=["cpro.baidu.com"],y=0,z=(new Date).getTime(),A=window.location.protocol||"http:",B="cc,cf,ci,ck,cl,cm,cp,cw,ds,ep,et,fl,ja,ln,lo,lt,nv,rnd,sb,se,si,st,su,sw,sse,v,u".split(",");function C(){if(typeof window["_bdhm_loaded_"+c.id]=="undefined")window["_bdhm_loaded_"+c.id]=g,this.a={},this.H=[],this.h={},this.A()}
C.prototype={w:function(){var a="";try{external.twGetVersion(external.twGetSecurityID(window))&&external.twGetRunPath.toLowerCase().indexOf("360se")>-1&&(a=17)}catch(b){}return a},e:function(a,b){var a=a.replace(/:\d+/,""),b=b.replace(/:\d+/,""),d=a.indexOf(b);return d>-1&&d+b.length==a.length},i:function(a,b){a=a.replace(/^https?:\/\//,"");return a.indexOf(b)==0},b:function(a){for(var b=0;b<c.dm.length;b++)if(c.dm[b].indexOf("/")>-1){if(this.i(a,c.dm[b]))return g}else{var d=n(a);if(d&&this.e(d,c.dm[b]))return g}return false},
s:function(){for(var a=window.location.hostname,b=0,d=c.dm.length;b<d;b++)if(this.e(a,c.dm[b]))return c.dm[b].replace(/(:\d+)?[\/\?#].*/,"");return a},t:function(){for(var a=0,b=c.dm.length;a<b;a++){var d=c.dm[a];if(d.indexOf("/")>-1&&this.i(window.location.href,d))return d.replace(/^[^\/]+(\/.*)/,"$2")+"/"}return"/"},z:function(){if(document.referrer)for(var a=function(a){for(var b=0,d=a[3]==2?a[1]+"/":"",e=a[3]==1?"."+a[1]:"",a=a[4].split(","),f=0,F=a.length;f<F;f++)if(a[f]!==""&&RegExp(d+a[f]+
e).test(document.referrer)){b=f+1;break}return b},b=function(a){if(/google.(com|cn)/.test(document.referrer)&&/(%25[0-9a-fA-F]{2}){2}/.test(a))try{a=decodeURIComponent(a)}catch(b){}if(/sogou.com/.test(document.referrer)&&/%u[0-9a-fA-F]{4}/.test(a))try{a=unescape(a)}catch(d){}for(var e=0,f=x.length;e<f;e++)document.referrer.indexOf(x[e])>-1&&(a="");return a},d=0,e=c.se.length;d<e;d++){if(RegExp(c.se[d][1]).test(document.referrer)){var f=m(document.referrer,c.se[d][2]);if(f)return this.a.se=c.se[d][0],
this.a.sse=a(c.se[d]),this.a.sw=b(f),2}}else return z-y>c.vdur?1:4;a=false;return(a=this.b(document.referrer)&&this.b(window.location.href)?g:this.e(n(document.referrer)||"",window.location.hostname))?z-y>c.vdur?1:4:3},getData:function(a){try{var b,d=RegExp("(^| )"+a+"=([^;]*)(;|$)").exec(document.cookie);if(!(b=d?d[2]:h)){var e;if(!(e=l(a)))a:{if(window.localStorage){var f=window.localStorage.getItem(a);if(f){var i=f.indexOf("|"),k=f.substring(0,i)-0;if(k&&k<(new Date).getTime()){e=f.substring(i+
1);break a}}}else if(w()){v.load(window.location.hostname);e=v.getAttribute(a);break a}e=h}b=e}return b}catch(E){}},setData:function(a,b,d){try{var e=this.s(),f=this.t(),i;d&&(i=new Date,i.setTime(i.getTime()+d));document.cookie=a+"="+b+(e?"; domain="+e:"")+(f?"; path="+f:"")+(i?"; expires="+i.toGMTString():"")+"";if(d){var k=new Date;k.setTime(k.getTime()+d||31536E6);if(window.localStorage){b=k.getTime()+"|"+b;try{window.localStorage.setItem(a,b)}catch(E){}}else if(w())v.expires=k.toUTCString(),
v.load(window.location.hostname),v.setAttribute(a,b),v.save(window.location.hostname)}else j(a,b)}catch(H){}},F:function(){var a,b,d,e;y=this.getData("Hm_lpvt_"+c.id)||0;b=this.z();a=b!=4?1:0;d=(d=this.getData("Hm_lvt_"+c.id))?Math.round((d-0)/1E3):"";this.setData("Hm_lvt_"+c.id,z,c.age);this.setData("Hm_lpvt_"+c.id,z);e=z==this.getData("Hm_lpvt_"+c.id)?"1":"0";if(c.nv==0&&this.b(window.location.href)&&(document.referrer==""||this.b(document.referrer)))a=0,b=4;this.a.nv=a;this.a.st=b;this.a.cc=e;
this.a.lt=d},D:function(){for(var a=[],b=0,d=B.length;b<d;b++){var e=B[b],f=this.a[e];typeof f!="undefined"&&f!==""&&a.push(e+"="+encodeURIComponent(f))}return a.join("&")},G:function(){this.F();this.a.si=c.id;this.a.su=document.referrer;this.a.ds=r;this.a.cl=s+"-bit";this.a.ln=q;this.a.ja=p?1:0;this.a.ck=o?1:0;this.a.lo=typeof _bdhm_top=="number"?1:0;var a=this.a,b="";if(navigator.plugins&&navigator.mimeTypes.length){var d=navigator.plugins["Shockwave Flash"];d&&d.description&&(b=d.description.replace(/^.*\s+(\S+)\s+\S+$/,
"$1"))}else if(window.ActiveXObject)try{if(d=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"))(b=d.GetVariable("$version"))&&(b=b.replace(/^.*\s+(\d+),(\d+).*$/,"$1.$2"))}catch(e){}a.fl=b;this.a.sb=this.w();this.a.v="1.0.24";a=window.location.href;this.a.cm=m(a,"hmmd")||"";this.a.cp=m(a,"hmpl")||"";this.a.cw=m(a,"hmkw")||"";this.a.ci=m(a,"hmci")||"";this.a.cf=m(a,"hmsr")||"";this.a.et=0;this.a.ep=""},A:function(){var a=this;try{a.G(),a.a.nv==0?a.C():a.g(".*"),a.f(),a.o(),a.q(),a.n&&a.n(),a.m&&a.m(),
a.d=new D,u(window,"beforeunload",a.B()),a.r(),window._hmt=a.h,a.h.push=function(){a.l.apply(a,arguments)}}catch(b){var d=[];d.push("si="+c.id);d.push("n="+encodeURIComponent(b.name));d.push("m="+encodeURIComponent(b.message));d.push("r="+encodeURIComponent(document.referrer));t(A+"//hm.baidu.com/hm.gif?"+d.join("&"))}},B:function(){var a=this;return function(){a.a.et=3;a.a.ep=(new Date).getTime()-a.d.j+","+((new Date).getTime()-a.d.c+a.d.k);a.f()}},f:function(){var a=this;a.a.rnd=Math.round(Math.random()*
2147483647);var b=A+"//hm.baidu.com/hm.gif?"+a.D();a.a.u?t(b):(a.p(b),t(b,function(b){a.g(b)}))},o:function(){if(c.icon!=""){var a,b=c.icon.split("|"),d="http://tongji.baidu.com/hm-web/welcome/ico?s="+c.id;a=(A=="http:"?"http://eiv":"https://bs")+".baidu.com"+b[0]+"."+b[1];switch(b[1]){case "swf":var e=b[2],b=b[3],d="s="+d,f="HolmesIcon"+z;a='<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" id="'+f+'" width="'+e+'" height="'+b+'"><param name="movie" value="'+a+'" /><param name="flashvars" value="'+
d+'" /><param name="allowscriptaccess" value="always" /><embed type="application/x-shockwave-flash" name="'+f+'" width="'+e+'" height="'+b+'" src="'+a+'" flashvars="'+d+'" allowscriptaccess="always" /></object>';break;case "gif":a='<a href="'+d+'" target="_blank"><img border="0" src="'+a+'" width="'+b[2]+'" height="'+b[3]+'"></a>';break;default:a='<a href="'+d+'" target="_blank">'+b[0]+"</a>"}document.write(a)}},q:function(){var a=window.location.hash.substring(1),b=RegExp(c.id),d=document.referrer.indexOf("baidu.com")>
-1?g:false;a&&b.test(a)&&d&&(b=document.createElement("script"),b.setAttribute("type","text/javascript"),b.setAttribute("charset","utf-8"),b.setAttribute("src",A+"//"+c.js+m(a,"jn")+"."+m(a,"sx")+"?"+this.a.rnd),a=document.getElementsByTagName("script")[0],a.parentNode.insertBefore(b,a))},l:function(a){if(a.length&&a.length>1&&a[0]=="_trackPageview"&&a[1].charAt&&a[1].charAt(0)=="/"){this.a.et=0;this.a.ep="";var b=this.a.u,d=this.a.su;this.a.u=A+"//"+window.location.host+a[1];this.a.su=window.location.href;
this.f();this.a.u=b;this.a.su=d}},r:function(){var a=window._hmt;if(a&&a.length&&a.shift)for(;a.length>0;)this.l(a.shift())},p:function(a){var b=l("Hm_unsent_"+c.id)||"",b=encodeURIComponent(a.replace(/^https?:\/\//,"")+"&u="+encodeURIComponent(window.location.href))+(b?","+b:"");j("Hm_unsent_"+c.id,b)},g:function(a){var b=l("Hm_unsent_"+c.id)||"";b&&((b=b.replace(RegExp(encodeURIComponent(a.replace(/^https?:\/\//,""))+"(%26u%3D[^,]*)?,?","g"),"").replace(/,$/,""))?j("Hm_unsent_"+c.id,b):(a="Hm_unsent_"+
c.id,window.sessionStorage&&window.sessionStorage.removeItem(a)))},C:function(){var a=this,b=l("Hm_unsent_"+c.id);if(b)for(var b=b.split(","),d=0,e=b.length;d<e;d++)t(A+"//"+decodeURIComponent(b[d]).replace(/^https?:\/\//,""),function(b){a.g(b)})}};function D(){this.c=this.j=(new Date).getTime();this.k=0;typeof document.I=="object"?(u(document,"focusin",G(this)),u(document,"focusout",G(this))):(u(window,"focus",G(this)),u(window,"blur",G(this)))}
function G(a){return function(b){if(!(b.target&&b.target!=window)){if(b.type=="blur"||b.type=="focusout")a.k+=(new Date).getTime()-a.c;a.c=(new Date).getTime()}}}new C;})();