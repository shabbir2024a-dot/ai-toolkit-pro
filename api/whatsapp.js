/**
 * 24/7 WhatsApp AI Bot Webhook & API Handler
 * Handles Meta WhatsApp Cloud API webhooks & direct API chat queries.
 */

const CONFIG = {
  businessName: "AI Toolkit Pro / Shabbir Ahmed AI Solutions",
  owner: "Shabbir Ahmed",
  phone: "+91 86386 28661",
  email: "shabbir2024a@gmail.com",
  address: "GS Road, Guwahati, Assam 781005",
  demoUrl: "https://ai-toolkit-pro-eta.vercel.app/whatsapp-demo",
  verifyToken: process.env.WHATSAPP_VERIFY_TOKEN || "SHABBIR_AI_TOKEN_2026"
};

function classifyIntent(text) {
  const msg = (text || '').toLowerCase().trim();
  if (!msg) return 'empty';
  if (/talk to (human|person|shabbir|owner|founder)|speak with|call me/i.test(msg)) return 'human_escalation';
  if (/demo|sample|show me|how it works|trial|test it|live link|preview/i.test(msg)) return 'demo_request';
  if (/price|pricing|cost|how much|rate|fees|charges/i.test(msg)) return 'pricing_inquiry';
  if (/clinic|doctor|opd|patient|prescription|dentist|dental|hospital/i.test(msg)) return 'clinic_saas';
  if (/salon|spa|hair|beauty|parlour|stylist|facial/i.test(msg)) return 'salon_booking';
  if (/shop|store|ecom|sell product|catalog|upi|order bot/i.test(msg)) return 'ecom_bot';
  if (/broadcast|bulk|marketing|outreach|blast/i.test(msg)) return 'bulk_broadcast';
  if (/meet|call|schedule|appointment|tomorrow|today|office|visit/i.test(msg)) return 'schedule_meeting';
  if (/location|address|where are you|guwahati|assam|gs road/i.test(msg)) return 'location_inquiry';
  if (/^(hi|hello|hey|namaste|assalam|salaam|good (morning|afternoon|evening))\b/i.test(msg)) return 'greeting';
  if (/thank|thanks|great|awesome|okay|ok|sure|alright/i.test(msg)) return 'gratitude';
  return 'general_inquiry';
}

function generateReply(text, senderName = "") {
  const intent = classifyIntent(text);
  const firstName = senderName ? senderName.split(' ')[0] : "";
  const greeting = firstName ? `Hi ${firstName}! ` : "Hello! ";

  switch (intent) {
    case 'greeting':
      return `${greeting}Welcome to ${CONFIG.businessName}. I am Shabbir Ahmed's 24/7 AI Assistant. 🤖⚡\n\nWe build turnkey WhatsApp AI Receptionists, Smart Booking Bots, and Clinic/Salon Automation systems right here in Guwahati.\n\nHow can I help your business today? You can ask me about:\n1️⃣ 24/7 WhatsApp AI Receptionist\n2️⃣ Clinic OPD & Prescription SaaS\n3️⃣ Interactive Live Demo\n4️⃣ Monthly Pricing (Starting ₹2,500/mo)\n\nWhat type of business do you run?`;

    case 'demo_request':
      return `You can try our interactive live WhatsApp AI Receptionist demo directly on your phone right now! 📲✨\n\n🔗 Live Demo: ${CONFIG.demoUrl}\n\nKey features in the demo:\n✅ Autonomous 24/7 reply under 3 seconds\n✅ Smart appointment booking & slot management\n✅ Zero missed leads guarantee\n\nWe also offer a 7-day risk-free pilot for local businesses in Guwahati. Would you like to schedule a 10-minute setup call?`;

    case 'pricing_inquiry':
      return `Here is our transparent pricing structure: 💰📋\n\n🤖 24/7 WhatsApp AI Receptionist: ₹2,500/month flat (No setup fee, includes 7-day free trial)\n🏥 Clinic OPD & Prescription SaaS: ₹4,999 one-time license\n🛍️ WhatsApp E-Commerce & UPI Bot: ₹3,999 one-time\n💇 Salon & Spa Booking System: ₹2,500/month\n📢 WhatsApp Bulk Broadcast Engine: ₹3,499 one-time\n\nAll plans include turnkey onboarding, custom AI training, and 24/7 support.\n\nWhich solution fits your current requirement best?`;

    case 'clinic_saas':
      return `Our Clinic OPD & Prescription SaaS is specially engineered for healthcare practices and doctors: 🏥🩺\n\n✨ Key Highlights:\n• Automated patient appointment booking via WhatsApp\n• Zero-paper digital OPD queue management\n• One-click digital prescription delivery directly to patient's WhatsApp\n• Automated appointment reminders (reduces no-shows by 45%)\n\n💰 Price: ₹4,999 one-time license (No heavy monthly software fees).\n\nWould you like a live walkthrough or to test our sample clinic bot?`;

    case 'salon_booking':
      return `Our Salon & Spa WhatsApp Booking System completely eliminates front-desk chaos: 💇💆\n\n✨ Highlights:\n• 24/7 automated stylist & treatment slot reservations\n• Instant WhatsApp confirmation & automated reminder 2 hours prior\n• UPI advance deposit collection to eliminate no-shows\n• Client retargeting broadcast for festive offers\n\n💰 Rate: ₹2,500/month flat.\n\nTry our interactive booking flow here: ${CONFIG.demoUrl}`;

    case 'ecom_bot':
      return `Our WhatsApp E-Commerce & UPI Order Bot turns your WhatsApp into a high-converting sales machine: 🛍️💳\n\n✨ Highlights:\n• Interactive product catalog directly inside WhatsApp\n• Automated cart management & address capture\n• Instant dynamic UPI QR code generator (PhonePe, GPay, Paytm)\n• Auto-sends payment receipt & updates your order log\n\n💰 Rate: ₹3,999 one-time setup.\n\nWould you like to see how product ordering works?`;

    case 'bulk_broadcast':
      return `Our WhatsApp Bulk Broadcast & Retargeting Engine helps you reach all your past customers safely: 📢📊\n\n✨ Highlights:\n• Intelligent Anti-Ban throttler with variable delays\n• Custom variable tags (e.g., Hi {Name}, your special offer...)\n• Lead group filtering & delivery analytics\n• Zero per-message fee\n\n💰 License: ₹3,499 one-time.\n\nWould you like us to demo the broadcasting engine for you?`;

    case 'schedule_meeting':
      return `I'd be delighted to set up a meeting with Shabbir Ahmed! 📅🤝\n\nWe can arrange:\n📍 In-person meeting at GS Road, Guwahati, Assam\n💻 Or a quick 10-minute Google Meet / Phone Call\n\nPlease reply with:\n1. Your preferred day & time\n2. The best number to reach you on\n3. Your business name\n\nShabbir will confirm your slot immediately!`;

    case 'location_inquiry':
      return `We are headquartered right on GS Road, Guwahati, Assam (781005). 📍🏢\n\nWe serve clinics, salons, coaching institutes, and retailers across Guwahati (Zoo Road, Christian Basti, Ulubari, Beltola, Six Mile) and deliver turnkey remote setups pan-India.\n\nWould you like an in-person demo at your location, or shall we connect over WhatsApp?`;

    case 'human_escalation':
      return `I have flagged your request directly for Shabbir Ahmed! 🔔👤\n\nHe has received your notification and will personally follow up with you shortly.\n\nDirect contact details:\n📞 Phone / WhatsApp: ${CONFIG.phone}\n✉️ Email: ${CONFIG.email}\n🌐 Website: https://ai-toolkit-pro-eta.vercel.app\n\nFeel free to leave any extra details about your project here in the meantime!`;

    case 'gratitude':
      return `You're very welcome! 😊 Whenever you're ready to automate your client bookings or test our 7-day free trial, just send a message here. Have a productive day! 🚀`;

    default:
      return `Thanks for reaching out! I am Shabbir Ahmed's 24/7 AI Assistant at AI Toolkit Pro Guwahati. 🤖\n\nWe provide turnkey WhatsApp AI Receptionists (₹2,500/mo) and custom automation systems that handle client inquiries and bookings 24/7 without missing a single lead.\n\nCheck out our live interactive demo here: ${CONFIG.demoUrl}\n\nCould you share a bit about your business or what you are looking to automate?`;
  }
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // 1. Meta Webhook Verification (GET)
  if (req.method === 'GET') {
    const mode = req.query['hub.mode'];
    const token = req.query['hub.verify_token'];
    const challenge = req.query['hub.challenge'];

    if (mode === 'subscribe' && token === CONFIG.verifyToken) {
      console.log("[WhatsApp Webhook] Verified challenge successfully!");
      return res.status(200).send(challenge);
    } else {
      return res.status(200).json({
        status: "active",
        bot: "24/7 WhatsApp AI Receptionist",
        business: CONFIG.businessName,
        phone: CONFIG.phone,
        owner: CONFIG.owner
      });
    }
  }

  // 2. Incoming Webhook or Chat API Query (POST)
  if (req.method === 'POST') {
    const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;

    // Check if Meta WhatsApp Cloud API payload format
    if (body?.object === 'whatsapp_business_account') {
      const entry = body.entry?.[0];
      const change = entry?.changes?.[0]?.value;
      const message = change?.messages?.[0];
      const contact = change?.contacts?.[0];

      if (message) {
        const fromPhone = message.from;
        const senderName = contact?.profile?.name || "Client";
        const incomingText = message.text?.body || "";
        const reply = generateReply(incomingText, senderName);

        console.log(`[Meta Cloud API] Incoming from ${fromPhone} (${senderName}): "${incomingText}" -> Reply generated.`);
        return res.status(200).json({ success: true, reply });
      }

      return res.status(200).send('EVENT_RECEIVED');
    }

    // Direct API Chat payload { message: "...", sender: "..." }
    const incomingText = body?.message || "";
    const senderName = body?.sender || "Client";
    const intent = classifyIntent(incomingText);
    const reply = generateReply(incomingText, senderName);

    return res.status(200).json({
      success: true,
      intent,
      reply,
      business: CONFIG.businessName,
      phone: CONFIG.phone
    });
  }

  return res.status(405).json({ error: "Method not allowed" });
}
