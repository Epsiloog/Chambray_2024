package fr.tathan.common.registry;

import net.fabricmc.fabric.api.gamerule.v1.GameRuleFactory;
import net.minecraft.world.level.GameRules;

public class GameRuleRegistry {

    /** On register une GameRule **/
    public static final GameRules.Key<GameRules.BooleanValue> SHOULD_PLAYER_ATTACK =
            net.fabricmc.fabric.api.gamerule.v1.GameRuleRegistry.register("shouldPlayerAttack", GameRules.Category.PLAYER, GameRuleFactory.createBooleanRule(false));

    public static void initialize() {
    }

}
