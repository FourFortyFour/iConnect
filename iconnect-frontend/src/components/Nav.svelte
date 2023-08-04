<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,700,1,0"
/>
<header class="navbar" id="navbar">
  <a href="/" class="icon-link">
    <img
      class="logo"
      src="/logos/logo-no-background.png"
      draggable="false"
      alt="logo"
    />
  </a>
  <nav>
    <ul class="nav__links">
      <li class="navitem"><a href="/contact">CONTACT</a></li>
      <li class="navitem"><a href="/order">GET YOUR OWN</a></li>
    </ul>
  </nav>
  <dt>
  </dt>
</header>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");
  * {
    box-sizing: border-box;
    margin: 0;
    font-family: "Cabin Condensed", sans-serif;
  }

  .navbar {
    position: sticky;
    top: 2vh;
    margin: 2vh 0.5vw 0;
    /* grid-area: 2/2/2/12; */

    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    background-color: #444444be;
    backdrop-filter: blur(20px);
    border-radius: 50px;

    transition: all 500ms ease-in-out 0s;
    user-select: none;
    z-index: 4;
    padding: 3vh 0;
  }

  .navbar:hover {
    background-color: #444444;
  }

  .navbar:n .nav__links {
    list-style: none;
  }

  .nav__links li {
    display: inline-block;
    padding: 0px 50px;
  }

  .nav__links li a {
    transition: all 500ms ease-in-out 0s;
  }

  .nav__links li a:hover {
    font-size: 30px;
    font-weight: 700px;
    color: #6ee2f5;
    letter-spacing: 10px;
  }

  .navitem,
  .navitem a {
    font-family: "Cabin Condensed";
    font-weight: 600px;
    font-size: 25px;
    color: #ffffff;
    text-decoration: none;
    letter-spacing: 7px;
  }

  .navitem a:hover {
    letter-spacing: 12px;
  }

  .logo {
    padding-left: 20px;
    width: 100%;

    cursor: pointer;
    user-select: none;
  }

  .icon-link {
    width: 5%;
  }

  /* .clearing {
    margin-bottom: 7%;
    opacity: 0%;
  } */
</style>
