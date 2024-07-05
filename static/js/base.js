// searchForm = document.querySelector('.search-form');
// document.querySelector('#search-btn').onclick =() => {
//     searchForm.classList.toggle('active');
// }


document.addEventListener("DOMContentLoaded", function() {
  let loginForm = document.querySelector('.login-form-container');
 
  document.querySelector("#login-btn").addEventListener("click", function() {
    loginForm.classList.toggle('active');
  });

});

document.getElementById('close-login-btn').addEventListener('click', function() {
  var loginPage = document.querySelector('.login-form-container');
  loginPage.style.display = 'none';

  // Redirect to home.html
  window.location.href = '/';
});
// Get the cancel button element
const cancelButton = document.querySelector('.cancel-button');

// Add a click event listener to the cancel button
cancelButton.addEventListener('click', function(event) {
  event.preventDefault(); // Prevent the default form submission behavior
  // Hide or remove the logout form from the page
  const logoutForm = document.querySelector('.logout-form');
  logoutForm.style.display = 'none'; // or logoutForm.remove();
  
});
// sing-up-form
const signUpForm = document.querySelector('.sign-up-form');

  // Add event listener for the keydown event
  document.addEventListener('keydown', function (event) {
    // Check if the pressed key is the "Escape" key
    if (event.key === 'Escape') {
      // Toggle the visibility of the sign-up form
      signUpForm.classList.toggle('hidden');
    }
});

// cut reviews burmese words short if more than 20
const textElement = document.getElementById('burmese-text');
const text = textElement.textContent;
const trimmedText = text.trim();
const words = trimmedText.split(/\s+/);
const visibleWords = words.slice(0, 20).join(' ');
const hiddenWords = words.slice(20).join(' ');
const output = `${visibleWords} <span class="hidden-text">${hiddenWords}</span> <span class="see-more" onclick="toggleHiddenText()">See More...</span>`;
textElement.innerHTML = output;

function toggleHiddenText() {
  const hiddenTextElement = document.getElementsByClassName('hidden-text')[0];
  const seeMoreElement = document.getElementsByClassName('see-more')[0];
  if (hiddenTextElement.style.display === 'none') {
    hiddenTextElement.style.display = 'inline';
    seeMoreElement.textContent = 'See Less';
  } else {
    hiddenTextElement.style.display = 'none';
    seeMoreElement.textContent = 'See More...';
  }
}

// book quote
const quoteContainer = document.getElementById('quote-container');
const quoteElement = document.getElementById('quote');
const authorElement = document.getElementById('author');

const quotes = [
  {
    quote: "Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.",
    author: "Neil Gaiman"
  },
  {
    quote: "You can never get a cup of tea large enough or a book long enough to suit me.",
    author: "C.S. Lewis"
  },
  {
    quote: "So, this is my life. And I want you to know that I am both happy and sad and I'm still trying to figure out how that could be.",
    author: "Stephen Chbosky"
  },
  {
    quote: "Do not read, as children do, to amuse yourself, or like the ambitious, for the purpose of instruction. No, read in order to live.",
    author: "Gustave Flaubert"
  },
  {
    quote: "When I was about eight, I decided that the most wonderful thing, next to a human being, was a book.",
    author: "Margaret Walker"
  },
  {
    quote: "I kept always two books in my pocket, one to read, one to write in.",
    author: "Robert Louis Stevenson"
  },
  {
    quote: "Once you have read a book you care about, some part of it is always with you.",
    author: "Louis L'Amour"
  },
  {
    quote: "We don’t need a list of rights and wrongs, tables of dos and don’ts: we need books, time, and silence",
    author: "Philip Pullman"
  },
  {
    quote: "Any book that helps a child to form a habit of reading, to make reading one of his deep and continuing needs, is good for him.",
    author: "Maya Angelou"
  },
  {
    quote: "Fiction is art and art is the triumph over chaos… to celebrate a world that lies spread out around us like a bewildering and stupendous dream.",
    author: "John Cheever"
  },
  {
    quote: "People don't realize how a man's whole life can be changed by one book.",
    author: "Malcolm X"
  },
  {
    quote: "Dare to love yourself.",
    author: "Author-Poet Aberjhani"
  },
  {
    quote: "Sit in a room and read--and read and read. And read the right books by the right people. Your mind is brought onto that level, and you have a nice, mild, slow-burning rapture all the time.",
    author: "Joseph Campbell"
  },
  {
    quote: "If you want to write a fantasy story with Norse gods, sentient robots, and telepathic dinosaurs, you can do just that. Want to throw in a vampire and a lesbian unicorn while you're at it? Go ahead. Nothing's off limits. But the endless possibility of the genre is a trap. It's easy to get distracted by the glittering props available to you and forget what you're supposed to be doing: telling a good story. Don't get me wrong, magic is cool. But a nervous mother singing to her child at night while something moves quietly through the dark outside her house? That's a story. Handled properly, it's more dramatic than any apocalypse or goblin army could ever be.",
    author: "Patrick Rothfuss"
  },
  {
    quote: "Maybe this is why we read, and why in moments of darkness we return to books: to find words for what we already know.",
    author: "Alberto Manguel"
  },
  {
    quote: "When a stargirl cries, she sheds not tears but light.",
    author: "Jerry Spinelli"
  },
  {
    quote: "I think the act of reading imbues the reader with a sensitivity toward the outside world that people who don't read can sometimes lack. I know it seems like a contradiction in terms; after all reading is such a solitary, internalizing act that it appears to represent a disengagement from day-to-day life. But reading, and particularly the reading of fiction, encourages us to view the world in new and challenging ways...It allows us to inhabit the consciousness of another which is a precursor to empathy, and empathy is, for me, one of the marks of a decent human being.",
    author: "John Connolly"
  },
  {
    quote: "Employ your time in improving yourself by other men's writings so that you shall come easilyby what others have labored hard for.",
    author: "Socrates"
  },
  {
    quote: "Indeed, learning to write may be part of learning to read. For all I know, writing comes out of a superior devotion to reading.",
    author: "Eudora Welty"
  },
  {
    quote: "There's a hunger for stories in all of us, adults too. We need stories so much that we're even willing to read bad books to get them, if the good books won't supply them.",
    author: "Philip Pullman"
  },
  {
    quote: "Focus on making yourself better, not on thinking that you are better.",
    author: "Bohdi Sanders"
  },
  {
    quote: "Nobody steals books but your friends.",
    author: "Roger Zelazny"
  },
  {
    quote: "There is no such thing as a child who hates to read; there are only children who have not found the right book.",
    author: "Frank Serafini"
  },
  {
    quote: "Books fall open, you fall in",
    author: "David McCord"
  },
  {
    quote: "Read. Read anything. Read the things they say are good for you, and the things they claim are junk. You'll find what you need to find. Just read.",
    author: "Neil Gaiman"
  },
  {
    quote: "Books. They are lined up on shelves or stacked on a table. There they are wrapped up in their jackets, lines of neat print on nicely bound pages. They look like such orderly, static things. Then you, the reader come along. You open the book jacket, and it can be like opening the gates to an unknown city, or opening the lid of a treasure chest. You read the first word and you're off on a journey of exploration and discovery.",
    author: "David Almond"
  },
  {
    quote: "Quiet people have the loudest minds.",
    author: "Stephen King"
  },
  {
    quote: "Books have a way of finding their way into our lives, usually, right when we need them the most.",
    author: "Richard Denney"
  },
  {
    quote: "To read is to empower",
    author: "Jane Evershed"
  },
  {
    quote: "Books didn’t make me wallow in darkness, darkness made me wallow in books.",
    author: "Jackson Pearce"
  },
  {
    quote: "The best of a book is not the thought which it contains, but the thought which it suggests; just as the charm of music dwells not in the tones but in the echoes of our hearts.",
    author: "Oliver Wendell Holmes Sr."
  }
];

// Function to generate a random quote
function generateRandomQuote() {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  const quote = quotes[randomIndex];
  quoteElement.textContent = quote.quote;
  authorElement.textContent = quote.author;
}

// Generate initial random quote
generateRandomQuote();


window.onscroll = () => {

    searchForm.classList.remove('active');

    if (window.scrollY > 80) {
        
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onload = () => {
    
    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    } else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}
