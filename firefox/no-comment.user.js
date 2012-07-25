// ==UserScript==
// @name No Comment
// @description Remove comments on news websites
// @version 0.4
// @match http://*.sudouest.fr/*
// @match http://*.humanite.fr/*
// @match http://*.nouvelobs.com/*
// @match http://*.ladepeche.fr/*
// @match http://*.clubic.com/*
// @match http://*.rue89.com/*
// @match http://*.dailymotion.com/*
// @match http://*.lesechos.fr/*
// @match http://*.youtube.com/*
// @match http://fr.news.yahoo.com/*
// @match http://*.lequipe.fr/*
// @match http://*.lemonde.fr/*
// @match http://*.leparisien.fr/*
// @match http://*.vimeo.com/*
// @match http://*.francefootball.fr/*
// @match http://*.lepoint.fr/*
// @match http://*.lefigaro.fr/*
// ==/UserScript==

GM_addStyle("@-moz-document domain(sudouest.fr) {     /* Remove comments from sudouest */ #comments {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(humanite.fr) {     /* Remove comments from humanite */ #comments, #comment_box, .comment_sep_number {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(nouvelobs.com) {     /* Remove comments from nouvelobs */ #reactions {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(ladepeche.fr) {     /* Remove comments from ladepeche */ #commentaires {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(clubic.com) {     /* Remove comments from clubic */ .comments {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(rue89.com) {     /* Remove comments from rue89 */ #commentaires {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(dailymotion.com) {     /* Remove comments from dailymotion */ #tab_comments_content, .tab_comments {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(lesechos.fr) {     /* Remove comments from lesechos */ .commentlist {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(youtube.com) {     /* Remove comments from youtube */ #watch-discussion {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(fr.news.yahoo.com) {     /* Remove comments from yahoo */ .yom-comments, #yom-comments {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(lequipe.fr) {     /* Remove comments from lequipe */ #commentaires {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(lemonde.fr) {     /* Remove comments from lemonde */ .reactions {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(leparisien.fr) {     /* Remove comments from leparisien */ #blocreactions {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(vimeo.com) {     /* Remove comments from vimeo */ #comments {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(francefootball.fr) {     /* Remove comments from francefootball */ .commentaires {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(lepoint.fr) {     /* Remove comments from lepoint */ #bloc_commentaire, .fermeture_commentaires {     display: none !important; }  } ");
GM_addStyle("@-moz-document domain(lefigaro.fr) {     /* Remove comments from lefigaro */ div.comment {     display: none !important; }  } ");
