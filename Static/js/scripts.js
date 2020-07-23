/*By morese */
/* Copyright 2020 @morese */

const nav = document.querySelector('.navbar');

window.onscroll = function() {
	var top = window.scrollY;

	if(top >= 50){
		nav.classList.add('active')
	}
	else{
		nav.classList.remove('active');
	}
}

