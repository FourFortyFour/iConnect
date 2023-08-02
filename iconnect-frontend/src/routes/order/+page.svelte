<script>
  import { enhance } from "$app/forms";
  export let data;
  console.log(data.product);
</script>

<div class="content">
  <aside />
  <main class="order-form">
    <h1>{data.product.name}</h1>
    <h2>{data.product.price}</h2>
    <p>{data.product.description}</p>
    <form action="?/pay" method="post" use:enhance>
      <label>
        Email:
        <input type="email" name="email" />
      </label>
      <label>
        Quantity:
        <input type="number" name="quantity">
      </label>
      <button>Buy Now</button>
    </form>
  </main>
  <aside />
</div>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
  }
  .content {
    display: flex;
  }
  .order-form {
    flex: 3;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    background-color: gainsboro;
  }

  form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  aside {
    flex: 1;
  }
</style>
