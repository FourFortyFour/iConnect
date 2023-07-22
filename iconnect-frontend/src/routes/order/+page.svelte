<script>
  import { enhance } from "$app/forms";
</script>

<div class="content">
  <aside />
  <main class="order-form">
    <h2>Place Your Order</h2>
    <form action="?/pay" method="post" use:enhance>
      <label>
        Email:
        <input type="email" name="email" />
      </label>
      <label>
        Quantity:
        <input type="number" name="quantity">
      </label>
      <button>Pay</button>
    </form>
  </main>
  <aside />
</div>

<style>
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
  aside {
    flex: 1;
  }
</style>
