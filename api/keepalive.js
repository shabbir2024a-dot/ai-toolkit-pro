module.exports = async (req, res) => {
  try {
    const start = Date.now();
    // Primary: Google Cloud Always Free Dedicated VPS (35.238.38.242)
    const targetUrl = process.env.WHATSAPP_BOT_HEALTH_URL || "http://35.238.38.242";
    const response = await fetch(targetUrl);
    const data = await response.json();
    return res.status(200).json({
      success: true,
      latencyMs: Date.now() - start,
      bot: data,
      endpoint: targetUrl,
      timestamp: new Date().toISOString()
    });
  } catch (err) {
    return res.status(500).json({
      success: false,
      error: err.message,
      timestamp: new Date().toISOString()
    });
  }
};
