<script>
</script>

<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li>Our Product</li>
    <li><a href="/contact">Contact</a></li>
    <li>About Us</li>
  </ul>
</nav>

<slot />

<footer>
  <section><span class="footer-start">2023 iConnect. All rights reserved</span></section>
  <section><span><img class="logo-footer" src="/logos/logo-no-background.png" alt="logo of iconnect"></span></section>
  <section class="toc">
    <a href="">Terms of Use</a>
    <a href="">Privacy Policy</a>
  </section>
</footer>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap');
  * {
    box-sizing: border-box;
    margin: 0;
    font-family: 'Cabin Condensed', sans-serif;
  }
  ul {
    display: flex;
    justify-content: space-around;
  }
  li {
    list-style: none;
    padding: 0 1%;
    color: white;
  }
  a {
    color: white;
    text-decoration: none;
  }
  nav {
    background-color: black;
    padding: 2% 0;
  }

  footer {
    background-color: black;
    display: flex;
    justify-content: space-between;
    padding: 1%;
    font-size: large;
  }

  .logo-footer {
    max-width: 30px;
  }

  .footer-start {
    color: white;
  }

  .toc {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
  }


</style>
