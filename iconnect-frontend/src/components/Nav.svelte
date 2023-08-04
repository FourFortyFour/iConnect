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
    <!-- <svg id="basket" class="basket" xmlns:xlink="http://www.w3.org/1999/xlink" width="65"
          viewBox="0 0 65 74" xmlns="http://www.w3.org/2000/svg" height="74">
          <g fill-rule="nonzero" fill="none">
              <path id="ketfill" class="ketfill"
                  d="M64.407 9.856L53.605 0H11.371L.569 9.856A1.548 1.548 0 00.1 11.603c.235.619.843 1.031 1.524 1.031h61.727a1.62 1.62 0 001.522-1.031 1.545 1.545 0 00-.467-1.747z"
                  fill="#C4C4C4"></path>
              <path id="ketfill2" class="ketfill2"
                  d="M63.351 9.927H1.624C.728 9.927 0 10.644 0 11.529v59.267C0 72.566 1.454 74 3.249 74h58.478c1.795 0 3.249-1.434 3.249-3.204V11.53c0-.885-.728-1.602-1.625-1.602z"
                  fill="#FFFFFF"></path>
              <path id="ketfill3" class="ketfill3"
                  d="M32.488 45.122c-7.963 0-14.44-6.447-14.44-14.37v-4.79a1.6 1.6 0 011.605-1.596 1.6 1.6 0 011.604 1.596v4.79c0 6.163 5.04 11.177 11.23 11.177 6.192 0 11.231-5.014 11.231-11.177v-4.79a1.6 1.6 0 011.604-1.596 1.6 1.6 0 011.605 1.596v4.79c0 7.923-6.477 14.37-14.44 14.37z"
                  fill="#aaaaaa"></path>
          </g>
      </svg> -->
    <!-- <div class="dp"></div> -->
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
    margin: 0 0.5vw;
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
