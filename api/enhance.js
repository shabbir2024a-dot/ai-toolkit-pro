export default async function handler(req, res) {
  // CORS configuration
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Parse prompt
  let prompt = '';
  if (req.method === 'POST') {
    const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    prompt = body?.prompt || '';
  } else if (req.method === 'GET') {
    prompt = req.query?.prompt || '';
  }

  if (!prompt || typeof prompt !== 'string' || !prompt.trim()) {
    return res.status(400).json({ error: 'Missing or empty prompt parameter' });
  }

  const apiKey = process.env.INCEPTION_API_KEY || 'sk_db07465bac7bf323d147b157f2572a18771318016466778be066ee5dd9898a1a';

  try {
    const response = await fetch('https://api.inceptionlabs.ai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'mercury-3',
        messages: [
          {
            role: 'system',
            content: 'You are an elite cinematic visual director and prompt expansion engine for AI imagery (Flux.1 / Midjourney). Expand the user idea into one vivid, hyper-detailed, photorealistic sentence specifying lighting, camera angle, textures, and cinematic depth. Return ONLY the enhanced prompt without commentary, quotes, or preambles.'
          },
          {
            role: 'user',
            content: prompt.trim()
          }
        ],
        max_tokens: 512,
        temperature: 0.7
      })
    });

    if (!response.ok) {
      const errText = await response.text();
      return res.status(response.status).json({ error: `Inception API error: ${errText}` });
    }

    const data = await response.json();
    const enhanced = data.choices?.[0]?.message?.content?.trim() || prompt;

    return res.status(200).json({
      success: true,
      enhanced,
      original: prompt,
      model: 'mercury-3',
      provider: 'Inception Labs (Parallel Diffusion LLM)'
    });
  } catch (error) {
    return res.status(500).json({
      error: error.message || 'Internal enhancement error',
      fallback: prompt
    });
  }
}
