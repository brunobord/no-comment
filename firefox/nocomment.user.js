// ==UserScript==
// @name No Comment
// @description Remove comments on news websites
// @version 0.1
// @match http://*.sudouest.fr/*
// @match http://*.lefigaro.fr/*
// @match http://fr.news.yahoo.com/*
// @match http://*.lemonde.fr/*
// ==/UserScript==

GM_addStyle("@-moz-document domain(sudouest.fr) {     /* Remove comments from sudouest */ #comments {     display: none; }  } ");
GM_addStyle("@-moz-document domain(lefigaro.fr) {     /* Remove comments from lefigaro */ div.comment {     display: none; }  } ");
GM_addStyle("@-moz-document domain(fr.news.yahoo.com) {     /* Remove comments from yahoo */ .yom-comments, #yom-comments {     display: none; }  } ");
GM_addStyle("@-moz-document domain(lemonde.fr) {     /* Remove comments from lemonde */ .reactions {     display: none; }  } ");
