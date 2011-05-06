/*
 * Only put stuff that works for every page in this file
 */
$(document).ready(function() {
  /* for each menu button, add target URL as the page to go to in
   * onclick handler for button */
  $(".menu_btn[target]").each(function(index,element){
    var target = $(element).attr("target");
    $(element).click(function(){ window.location = target; });
  });
});
