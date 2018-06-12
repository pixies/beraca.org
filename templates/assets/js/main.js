/* --------------------------------------------
  DOCUMENT.READY
--------------------------------------------- */
$(document).ready(function(){
  'use strict';

  window.sr = ScrollReveal({ reset: false, mobile: true });

  var rightLight = {
    origin   : "right",
    distance : "0.5em",
    duration : 200,
    scale    : 3.05,
  }
  var topLight = {
    origin   : "top",
    distance : "0em",
    duration : 1000,
    delay    : 1000,
    scale    : 1,
  }
  var topLightRotate = {
    origin   : "top",
    distance : "0em",
    duration : 1000,
    delay    : 1500,
    scale    : 2,
  }
  var ShowQuickly = {
    origin   : "top",
    distance : "0em",
    duration : 100,
    delay    : 500,
    scale    : 2,
  }
  var topLightSlow = {
    origin   : "top",
    distance : "0em",
    duration : 300,
    delay    : 1300,
    scale    : 1,
  }
  var topLightVerySlow = {
    origin   : "top",
    distance : "0em",
    duration : 300,
    delay    : 2000,
    scale    : 1,
  }
  var background = {
    origin   : "bottom",
    distance : "0em",
    duration : 300,
    delay    : 100,
    scale    : 1,
  }

  var block = {
    reset: true,
    viewOffset: { top: 64 }
  }

  sr.reveal(".s01, .s02, .s03", topLight)
  sr.reveal(".scene-background-purple", background)
  sr.reveal(".scene-city", topLight)
  sr.reveal(".scene-entrepreneur", topLightSlow)
  sr.reveal(".scene-text-reparte-1", topLight)
  sr.reveal(".scene-world", topLight)
  sr.reveal(".scene-world-trace-1, .scene-world-trace-2, .scene-world-trace-3", topLightVerySlow)
  sr.reveal(".scene-text-reparte-2, .scene-text-reparte-3, .scene-text-reparte-4", topLight)
  sr.reveal(".scene-ibcommunity-states, .scene-ibcommunity-communities, .scene-ibcommunity-families", topLight)
  sr.reveal(".avatar-people, .scene-eolic", topLight)
  sr.reveal(".scene-eolic", topLightRotate)
  sr.reveal(".scene-cloud, .scene-text-reparte-5", topLight)
  sr.reveal(".scene-itens, .scene-windmill, .scene-windmill-an", ShowQuickly)
  sr.reveal(".scene-text-reparte-6, .scene-how-it-works", topLight)
  sr.reveal(".scene-text-reparte-7,.scene-text-reparte-8,.scene-text-reparte-9,.scene-text-reparte-10,.scene-text-reparte-11,.scene-text-reparte-12 ", topLight)
  sr.reveal(".scene-invest-title, .scene-investment, .scene-text-reparte-13, .scene-text-reparte-14, .scene-text-reparte-15, .scene-sign-in ", topLight)



});
