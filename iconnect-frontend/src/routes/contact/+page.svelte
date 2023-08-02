<main>
  <div class="contact-header">
    <div class="hbar" />
    <h1>CONTACT</h1>
    <div class="hbar" />
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
      <label for="msg">
        <textarea
          name="msg"
          id=""
          cols="30"
          rows="10"
          placeholder="Message"
          required
        />
      </label>
      <button>Send</button>
    </form>
    <img
      class="contact-mainimage"
      src="/svgs/contactpage.svg"
      alt="contact us"
    />
  </section>
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    margin: 0px;
    font-family: "Cabin Condensed", sans-serif;
  }
  h1 {
    margin: 0;
  }
  main {
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
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .hbar {
    flex-grow: 1;
    height: 5px;
    background-color: rgb(225, 6, 6);
    border-radius: 5px;
    margin: 0 10px;
  }

  .contact-mainimage {
    flex: 0.4;
    display: flex;
    justify-content: center;
  }

  label {
    width: 70%;
    margin-bottom: 2%;
  }

  input {
    font-size: 18px;
    border-radius: 25px;
    width: 100%;
    border: 0.05px solid black;
    padding: 2%;
  }

  textarea {
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
