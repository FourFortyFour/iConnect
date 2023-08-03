<footer>
  <section>
    <span class="footer-start">2023 iConnect. All rights reserved</span>
  </section>
  <section>
    <img
      class="logo-footer"
      src="/svgs/radiantlogo.svg"
      alt="logo of iconnect"
    />
  </section>
  <section class="terms_n_conditions">
    <a href="*">Terms of Use</a>
    <a href="*">Privacy Policy</a>
  </section>
</footer>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");
  * {
    box-sizing: border-box;
    margin: 0;
    font-family: "Cabin Condensed", sans-serif;
    /* position: relative; */
  }
  a {
    text-decoration: none;
    color: white;
  }
  footer {
    background-color: black;
    display: flex;
    justify-content: space-around;
    padding: 0.5em;
    font-size: large;
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 2.5rem;
  }

  .logo-footer {
    height: 2vw;
    width: 2vw;
  }

  .footer-start {
    color: white;
  }

  .terms_n_conditions {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
  }
</style>
