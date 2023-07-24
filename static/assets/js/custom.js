
// Toggle "expanded" class on the answer text to show/hide the full content
const answerContent = document.querySelector('.answer .q-text');
const toggleMore = () => {
  answerContent.classList.toggle('expanded');
};
answerContent.addEventListener('click', toggleMore);
answerContent.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    toggleMore();
  }
});
