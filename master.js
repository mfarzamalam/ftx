$('.how-we-get').owlCarousel({
	loop:true,
	margin:10,
	nav:true,
	autoplay:true,
	autoplayTimeout:2000,
	autoplayHoverPause:true,
	navText: ['<i class="text-white fa-solid fa-circle-arrow-left pe-2"></i>', '<i class="text-white fa-solid fa-circle-arrow-right"></i>'],
	responsive:{
		0:{
			items:1
		},
		600:{
			items:2
		},
		1000:{
			items:2
		}
	}
});







