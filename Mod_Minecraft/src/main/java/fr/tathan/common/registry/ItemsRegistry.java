package fr.tathan.common.registry;

import fr.tathan.TelluckyBlock;
import net.minecraft.core.Registry;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;

public class ItemsRegistry {

    /** On register un Item avec notre methode custom
     *
     * On utilise une class de MC (BlockItem) qui permet de créer un item qui pose un block
     *
     **/
    public static final Item TELLUCKY_ITEM = register(
            new BlockItem(BlocksRegistry.TELLUCKY_BLOCK, new Item.Properties()),
            "tellucky_block"
    );

    /** Une méthode qui permet d'ajouter notre item dans la liste des items de Minecraft **/
    public static Item register(Item item, String id) {
        ResourceLocation itemID = new ResourceLocation(TelluckyBlock.MODID, id);
        Item registeredItem = Registry.register(Registry.ITEM, itemID, item);
        return registeredItem;
    }

    /** Method pour initialisé les items **/
    public static void initialize() {
    }
}
