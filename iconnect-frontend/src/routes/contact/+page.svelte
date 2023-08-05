<script>
  import Spacer from "../../components/LandingPageAssests/Spacer.svelte";
</script>

<main>
  <Spacer />
  <div class="contact-header">
    <h1>CONTACT US</h1>
    <img class="contactimg" src="/imgs/icon-contact.png" alt="" />
  </div>
  <section>
    <form action="" method="post">
      <label for="name">
        <input type="text" name="name" placeholder="Enter your name" />
      </label>
      <label for="email">
        <input
          type="email"
          name="email"
          placeholder="email@mail.com"
          required
        />
      </label>
      <label for="phonenum">
        <input
          type="number"
          name="phonenum"
          placeholder="+971501234567"
          required
        />
      </label>
      <label for="msg">
        <input
          name="msg"
          id="user-message"
          cols="30"
          rows="10"
          placeholder="Message"
          required
        />
      </label>
      <button>Send</button>
    </form>
  </section>
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
  }

  main {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  section {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
  }

  section > * {
    padding: 4%;
  }

  form {
    display: flex;
    flex-direction: column;
    flex: 1;
    align-items: center;
  }

  .contact-header {
    margin-top: 1em;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .contactimg {
    width: 5vw;
  }

  label {
    width: 60vw;
    margin-bottom: 1%;
  }

  input {
    font-size: 18px;
    border-radius: 25px;
    width: 100%;
    border: 0.05px solid black;
    padding: 2%;
  }

  #user-message {
    font-size: 18px;
    border-radius: 25px;
    width: 100%;
    border: 0.05px solid black;
    padding: 2%;
  }

  button {
    background-color: black;
    color: white;
    border: none;
    font-size: 16px;
    padding: 2% 6%;
    border-radius: 25px;
  }
</style>
