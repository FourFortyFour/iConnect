<script>
    let currentDate = new Date().toLocaleDateString('en-US');

    let contactInfo = {
        email: 'contact@example.com',
        phone: '+1234567890'
    };
</script>

<style>
    /* Your CSS styles here */
</style>

<div class="container">
    <h1>Privacy Policy</h1>
    <p>Last Updated: {currentDate}</p>

    <h2>Privacy Policy for iConnect</h2>
    <p>Welcome to iConnect! At iConnect, we value your privacy and are committed to protecting your personal information. This Privacy Policy outlines how we collect, use, disclose, and protect your information when you visit our website or use our services.</p>

    <h2>Information We Collect</h2>
    <p>We may collect personal information that you provide to us when you interact with our website or services. This information may include:</p>
    <ul>
        <li>Contact information: Name, email address, phone number.</li>
        <li>Business details: Business name, industry, location.</li>
        <li>Payment information: Billing and payment details.</li>
        <li>Usage data: Information about how you use our website and services.</li>
    </ul>

    <h2>How We Use Your Information</h2>
    <p>We use the information we collect for various purposes, including but not limited to:</p>
    <ul>
        <li>Providing and improving our services.</li>
        <li>Processing transactions and sending notifications.</li>
        <li>Responding to your inquiries and providing customer support.</li>
        <li>Sending promotional materials and updates about our services.</li>
        <li>Complying with legal obligations.</li>
    </ul>

    <!-- More sections of the Privacy Policy go here... -->

    <h2>Contact Us</h2>
    <p>If you have any questions about this Privacy Policy, your rights, or our data practices, please contact us at <a href={`mailto:${contactInfo.email}`}>{contactInfo.email}</a> or {contactInfo.phone}.</p>

    <p><em>Legal Disclaimer: This Privacy Policy is provided for informational purposes only and is not intended as legal advice. For legal advice regarding GDPR compliance, please consult with a qualified legal professional.</em></p>
</div>
