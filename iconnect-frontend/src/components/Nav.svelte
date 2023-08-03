<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,700,1,0"
/>
<nav>
  <div class="content">
    <section class="head">
      <a href="/">
        <img
          class="main-logo"
          src="/logos/logo-no-background.png"
          alt="iconnect-logo"
        />
      </a>
    </section>
    <section class="links">
      <ul>
        <li class="link-btn">
          <span class="material-symbols-outlined">light_mode </span>
        </li>
        <a href="/contact" class="contact-btn link-btn">
          <li class="">Contact</li>
        </a>
        <a href="/order" class="cart-btn link-btn">
          <li class="link-btn">
            Cart<span class="material-symbols-outlined cart-icon">
              shopping_cart
            </span>
          </li>
        </a>
      </ul>
    </section>
  </div>
  <div class="grad" />
</nav>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");
  * {
    box-sizing: border-box;
    margin: 0;
    font-family: "Cabin Condensed", sans-serif;
  }
  .links {
    width: 100%;
  }
  ul {
    display: flex;
    width: 100%;
    justify-content: end;
  }
  li {
    list-style: none;
    padding: 0 1%;
    color: white;
  }

  .main-logo {
    max-width: 10%;
  }
  a {
    color: white;
    text-decoration: none;
  }
  .content {
    display: flex;
    align-items: center;
    padding: 1%;
  }
  nav {
    background-color: black;
    display: flex;
    flex-direction: column;
  }

  .grad {
    background: rgb(110, 226, 245);
    background: linear-gradient(
      90deg,
      rgb(194, 114, 237) 10%,
      rgb(7, 151, 234) 50%,
      rgb(194, 114, 237) 100%
    );
    padding: 0.5%;
  }

  .link-btn {
    padding: 1% 3%;
    border-radius: 25px;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 0px 0.5%;
  }

  .contact-btn {
    background: rgb(110, 226, 245);
    background: linear-gradient(
      180deg,
      rgba(110, 226, 245, 1) 0%,
      rgba(164, 0, 255, 1) 100%
    );
  }

  .contact-btn:hover {
    background: black;
    border: 2px solid #6ee2f5;
  }

  .cart-btn {
    border: 2px solid #6ee2f5;
  }

  .cart-icon {
    margin: 0px 10%;
  }
</style>
