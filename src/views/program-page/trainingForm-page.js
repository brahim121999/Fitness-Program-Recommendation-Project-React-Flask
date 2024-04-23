import { useState } from 'react';
import { Box, Button, Checkbox, FormControl, FormControlLabel, FormGroup, FormLabel, Grid, TextField, Typography, MenuItem } from '@mui/material';
import axios from 'axios';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';

const ingredientsList = [
    'Légumes frais (carottes, brocolis, épinards, etc.)',
    'Fruits frais (pommes, bananes, fraises, etc.)',
    'Viandes maigres (poulet, dinde, poisson, etc.)',
    'Produits laitiers (yaourt, fromage, lait, etc.)',
    'Céréales et grains (riz, pâtes, quinoa, etc.)',
    'Noix et graines (amandes, noix, graines de chia, etc.)',
    'Légumineuses (haricots, lentilles, pois chiches, etc.)',
    "Huiles et vinaigres (huile d'olive, vinaigre balsamique, etc.)",
    'Épices et assaisonnements (sel, poivre, origan, etc.)',
  ];
  
  const equipmentList = [
    'Haltères',
    'Kettlebells',
    'Barres de poids',
    'Banc de musculation',
    'Tapis de yoga',
    'Corde à sauter',
    'Ballon de stabilité',
    'Bande de résistance',
    'Machine elliptique',
    'Tapis de course',
    'Vélo stationnaire',
    'Step aérobique',
  ];
  

const TrainingForm = () => {
  const navigate = useNavigate();
  const [objective, setObjective] = useState('');
  const [ingredients, setIngredients] = useState([]);
  const [materials, setMaterials] = useState([]);
  const [trainingTimes, setTrainingTimes] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Envoi des données au backend avec Axios
      const response = await axios.post('http://127.0.0.1:5000/handle-query', {
        question: {
          objective, 
          ingredients, 
          materials, 
          trainingTimes, 
        },
        user_id: "1", 
      });
      console.log('Réponse du serveur:', response.data);
      toast.success('Connexion réussie ! Bienvenue à bord.');
      navigate('/');
      // Réinitialiser le formulaire après soumission réussie si nécessaire
      setObjective('');
      setIngredients([]);
      setMaterials([]);
      setTrainingTimes('');
    } catch (error) {
      console.error('Erreur lors de la soumission du formulaire:', error);
    }
  };

  const handleIngredientChange = (event) => {
    const { value } = event.target;
    setIngredients(
      ingredients.includes(value)
        ? ingredients.filter((item) => item !== value)
        : [...ingredients, value]
    );
  };

  const handleEquipmentChange = (event) => {
    const { value } = event.target;
    setMaterials(
      materials.includes(value)
        ? materials.filter((item) => item !== value)
        : [...materials, value]
    );
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Choisissez vos préférences d'entraînement
      </Typography>
      <form onSubmit={handleSubmit}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Objectif d'entraînement</FormLabel>
              <TextField
                fullWidth
                select
                variant="outlined"
                value={objective}
                onChange={(e) => setObjective(e.target.value)}
              >
                <MenuItem value="Perte de poids">Perte de poids</MenuItem>
                <MenuItem value="Gain de masse musculaire">Gain de masse musculaire</MenuItem>
                <MenuItem value="Amélioration de l'endurance">Amélioration de l'endurance</MenuItem>
              </TextField>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Ingrédients disponibles dans votre réfrigérateur</FormLabel>
              <FormGroup>
                {ingredientsList.map((ingredient) => (
                  <FormControlLabel
                    key={ingredient}
                    control={<Checkbox checked={ingredients.includes(ingredient)} onChange={handleIngredientChange} value={ingredient} />}
                    label={ingredient}
                  />
                ))}
              </FormGroup>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Matériaux disponibles</FormLabel>
              <FormGroup>
                {equipmentList.map((equipment) => (
                  <FormControlLabel
                    key={equipment}
                    control={<Checkbox checked={materials.includes(equipment)} onChange={handleEquipmentChange} value={equipment} />}
                    label={equipment}
                  />
                ))}
              </FormGroup>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Nombre de séances d'entraînement par semaine</FormLabel>
              <TextField
                fullWidth
                select
                variant="outlined"
                value={trainingTimes}
                onChange={(e) => setTrainingTimes(e.target.value)}
              >
                <MenuItem value="1">1 fois par semaine</MenuItem>
                <MenuItem value="2">2 fois par semaine</MenuItem>
                <MenuItem value="3">3 fois par semaine</MenuItem>
                {/* Ajoutez plus d'options selon vos besoins */}
              </TextField>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary">
              Soumettre
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
};

export default TrainingForm;

